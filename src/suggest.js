import "./app.css";
import Suggest from "./lib/Suggest.svelte";

const suggest = new Suggest({
    target: document.getElementById("suggest"),
});


export default suggest;
