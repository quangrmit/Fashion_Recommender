import "./app.css";
import Team from "./lib/Team.svelte";

const team = new Team({
    target: document.getElementById("team"),
});

export default team;
