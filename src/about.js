import "./app.css";
import About from "./lib/About.svelte";

const about = new About({
    target: document.getElementById("about"),
});

export default about;
