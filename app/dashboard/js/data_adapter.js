class DataAdapter {
    constructor(dataPath) {
        this.dataPath = dataPath;
        this.data = null;
        this.currentIndex = 0;
        this.isPlaying = false;
        this.listeners = [];
        this.playbackSpeed = 1; // 1x = real time (250Hz UI fs)
        this.intervalId = null;
    }

    async load() {
        try {
            const response = await fetch(this.dataPath);
            this.data = await response.json();
            console.log(`Loaded dataset: ${this.data.metadata.dataset}`);
            return true;
        } catch (e) {
            console.error("Failed to load data payload:", e);
            return false;
        }
    }

    addListener(callback) {
        this.listeners.push(callback);
    }

    start() {
        if (!this.data) return;
        this.isPlaying = true;
        
        const ui_fs = this.data.metadata.ui_fs; 
        const intervalMs = 1000 / ui_fs; // ms per sample

        // We use requestAnimationFrame in the main loop to render, 
        // but here we just advance the index to simulate real-time streaming buffer.
        
        let lastTime = performance.now();
        const loop = (currentTime) => {
            if (!this.isPlaying) return;
            
            const deltaTime = currentTime - lastTime;
            const samplesToAdvance = Math.floor(deltaTime / intervalMs) * this.playbackSpeed;
            
            if (samplesToAdvance > 0) {
                lastTime = currentTime;
                
                for(let i=0; i<samplesToAdvance; i++) {
                    const frame = this.getFrame(this.currentIndex);
                    this.listeners.forEach(cb => cb(frame));
                    
                    this.currentIndex++;
                    if (this.currentIndex >= this.data.metadata.length) {
                        this.currentIndex = 0; // Loop seamlessly
                    }
                }
            }
            this.intervalId = requestAnimationFrame(loop);
        };
        
        this.intervalId = requestAnimationFrame(loop);
    }

    stop() {
        this.isPlaying = false;
        if(this.intervalId) cancelAnimationFrame(this.intervalId);
    }

    getFrame(index) {
        // Return a normalized MonitoringFrame
        const qrs = this.data.waveforms.qrs_peaks || [];
        return {
            index: index,
            fhr: this.data.vitals.fhr_bpm,
            mhr: this.data.vitals.mhr_bpm,
            sqi: this.data.vitals.sqi,
            ehg: this.data.vitals.ehg_activity,
            abdominal: this.data.waveforms.abdominal[index],
            maternal_ref: this.data.waveforms.maternal_ref[index],
            maternal_est: this.data.waveforms.maternal_est[index],
            fetal_est: this.data.waveforms.fetal_est[index],
            is_qrs: qrs.includes(index)
        };
    }
}
