import { html, unsafeCSS, type HTMLTemplateResult } from "lit";
import { customElement } from "lit/decorators.js";
import { Counter } from "../models/counter";


import styled from '../styles/counter.css?inline';


@customElement('x-counter')
export class XCounter extends Counter {
    static styles = unsafeCSS(styled);

    protected render(): HTMLTemplateResult {
        return html`
            <h1>${ this.value }</h1>
            <button @click=${ this.__increment }> + </button>
            <button @click=${ this.__reset }> RESET </button>
            <button @click=${ this.__decrement }> - </button>
        `;
    }
}
