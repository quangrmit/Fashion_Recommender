<script>
    import Generator from "./Generator.svelte";
</script>

<nav>
    <div class="brand">What</div>
    <ul>
        <li><a href="#">Menu</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Team</a></li>
    </ul>
    <button>Open</button>
</nav>

<style>
    @font-face {
        font-family: "Valkocapela";
        src: url("./src/assets/VALKOCAPELA.woff");
    }
    * {
        font-family: "Valkocapela";
    }
    nav {
        position: absolute;
        top: 3vh;
        left: 3vw;
        display: flex;
        width: 91vw;
        justify-content: space-between;
        align-items: flex-start;
        z-index: 3;
    }
    nav > ul {
        display: flex;
        min-width: 30vw;
        justify-content: space-evenly;
    }
    nav li {
        list-style-type: none;
    }
    nav li > a {
        color: white;
        text-decoration: none;
    }
    .brand {
        color: white;
        font-size: xx-large;
    }
</style>
