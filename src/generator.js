import "./app.css";
import Generator from "./lib/Generator.svelte";

const generator = new Generator({
    target: document.getElementById("generator"),
});

export default generator;
