import { state } from "lit/decorators.js";
import { LitElement } from "lit";


export class Counter extends LitElement {
    @state() value = 0;

    __increment(): void { this.value++; }
    __reset(): void { this.value = 0; }
    __decrement(): void { this.value--; }
}
