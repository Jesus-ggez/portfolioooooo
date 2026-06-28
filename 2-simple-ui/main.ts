import { XCounter } from './src/components/xCounter';


declare global {
    interface HTMLElementTagNameMap {
        'x-counter': XCounter;
    }
}
