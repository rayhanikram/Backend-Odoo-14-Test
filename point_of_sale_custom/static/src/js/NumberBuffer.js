odoo.define('point_of_sale_custom.NumberBufferExtension', function (require) {
    'use strict';

    const NumberBuffer = require('point_of_sale.NumberBuffer');

    const INPUT_KEYS = new Set(
        ['Delete', 'Backspace', '+1', '+2', '+5', '+10', '+20', '+50', '+10000', '+20000', '+50000'].concat('0123456789+-.,'.split(''))
    );
    const CONTROL_KEYS = new Set(['Enter', 'Esc']);
    const ALLOWED_KEYS = new Set([...INPUT_KEYS, ...CONTROL_KEYS]);
    const originalHandleInput = NumberBuffer._handleInput;

    NumberBuffer._onInput = function (keyAccessor){
        return () => {
            if (this.eventsBuffer.length <= 2) {
                for (let event of this.eventsBuffer) {
                    if (!ALLOWED_KEYS.has(keyAccessor(event))) {
                        this.eventsBuffer = [];
                        return;
                    }
                }
                for (let event of this.eventsBuffer) {
                    this._handleInput(keyAccessor(event));
                    event.preventDefault();
                    event.stopPropagation();
                }
            }
            this.eventsBuffer = [];
        };
    };
    NumberBuffer._handleInput = function (key) {
        console.log(key)
        if (INPUT_KEYS.has(key)) {
            this._updateBuffer(key);  

            if (this.config && this.config.triggerAtInput) {
                this.component.trigger(this.config.triggerAtInput, { buffer: this.state.buffer, key });
            }
        } else {
            originalHandleInput.call(this, key);    
        }
    };


});