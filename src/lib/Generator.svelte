<script>
    import Navbar from "./Navbar.svelte";
    import axios from "axios";
    import MainApp from "../MainApp.svelte";

    let styles = [
        "Parisian style",
        "Athleisure style",
        "Classic style",
        "Lolita style",
        "Streetwear style",
        "Business Casual style",
        "Vintage style",
        "Chic style",
        "bohemian chic style",
        "Preppy style",
        "Punk style",
        "Punk style",
        "Tomboy style",
        "Gothic style",
        "Rocker style",
        "Ethnic style",
        "Girly style",
        "Kawaii style",
    ];
    let prompt = "";
    let moreDetails = "";
    let imageData;
    let male = false;
    let female = false;
    let casual = false;
    let formal = false;
    let loading = false;
    // let link = "https://190a-34-83-63-151.ngrok.io/image";
    let link = "https://dog.ceo/api/breeds/image/random";

    // const fetchImage = (async () => {
    //     const response = await fetch(link);
    //     console.log(response);

    //     return await response.json();
    // })();
    const fetchImage = async (prompt) => {
        loading = true;
        console.log(prompt);
        // const response = await axios.get(prompt);

        // console.log(response);
        // imageData = response.data;
        loading = false;
    };

    // const fetchImage = async () => {
    //     const response = await fetch(link);
    //     console.log(response);
    //     imageData = await response.json();
    // };

    function chooseMale() {
        male = true;
        female = false;
    }

    function chooseFemale() {
        female = true;
        male = false;
    }

    function chooseCasual() {
        casual = true;
        formal = false;
    }

    function chooseFormal() {
        formal = true;
        casual = false;
    }
    // full body of a male model wearing a winter outfit with parisian style
    /**
     * @param {boolean} [season]
     * @param {boolean} [trending]
     */
    function generatePrompt(season, trending) {
        let seasonString = "";
        let trendingString = "";
        let gender = "";
        console.log(formal);
        if (male == false && female == false) {
            gender = ["male", "female"][Math.floor(Math.random() * 2)];
        } else {
            male == true ? (gender = "male") : (gender = "female");
        }

        let style = "";
        if (casual == false && formal == false) {
            style = ["casual", "formal"][Math.floor(Math.random() * 2)];
        } else {
            casual == true ? (style = "casual") : (style = "formal");
        }

        if (season) {
            let month = new Date().getMonth();
            if (month == 0 || month == 1 || month == 2) seasonString = "spring";
            if (month == 3 || month == 4 || month == 5) seasonString = "summer";
            if (month == 6 || month == 7 || month == 8) seasonString = "autumn";
            if (month == 9 || month == 10 || month == 11) seasonString = "winter";
        }
        if (trending) {
            trendingString = "with " + styles[Math.floor(Math.random() * styles.length)];
        }

        let prompt = `full body of a ${gender} model wearing a ${style} ${seasonString} outfit ${trendingString}`;

        console.log(prompt);
        moreDetails = "";

        return prompt;
    }
</script>

<div class="body">
    <Navbar />
    <div class="grid-container">
        <div class="left">
            <div class="style">
                <div
                    class="button"
                    on:click={() => {
                        fetchImage(generatePrompt(false, true));
                    }}
                >
                    <p>🔥 TRENDING FIT</p>
                </div>

                <div
                    class="button"
                    on:click={() => {
                        fetchImage(generatePrompt(true, false));
                    }}
                >
                    <p>❄️ SEASON FIT</p>
                </div>
            </div>

            <div class="placeholder">
                {#if loading}
                    <section class="loader">
                        <div style="--i:0" class="slider" />
                        <div style="--i:1" class="slider" />
                        <div style="--i:2" class="slider" />
                        <div style="--i:3" class="slider" />
                        <div style="--i:4" class="slider" />
                    </section>
                {/if}

                {#if imageData == null}
                    <img src="src\assets\placeholder.png" alt="" />
                {:else}
                    <img src={imageData.message} alt="" />
                {/if}
                <!-- {#await fetchImage}
                    <p>...waiting</p>
                {:then data}
                    <img src={data.message} alt="Dog image" />
                {:catch error}
                    <p>An error occurred!</p>
                {/await} -->
            </div>
        </div>

        <div class="right">
            <div class="title">CUSTOMIZE</div>

            <div class="yourgender wrapper">
                <p>YOUR <br />GENDER</p>

                <div class="button-container">
                    <label class="container  {male ? 'active' : ' '}" on:click={chooseMale}>
                        MALE
                        <!-- <input type="radio" checked={true} name="radio" /> -->
                        <input type="radio" name="radio" />
                        <span class="checkmark" />
                    </label>

                    <label class="container {female ? 'active' : ' '}" on:click={chooseFemale}
                        >FEMALE
                        <input type="radio" name="radio" />
                        <span class="checkmark" />
                    </label>
                </div>
            </div>

            <div class="yourstyle wrapper">
                <p>YOUR <br />STYLE</p>

                <div class="button-container">
                    <label class="container {casual ? 'active' : ' '}" on:click={chooseCasual}
                        >CASUAL
                        <input type="radio" checked={true} name="radio" />
                        <span class="checkmark" />
                    </label>

                    <label class="container {formal ? 'active' : ' '}" on:click={chooseFormal}
                        >FORMAL
                        <input type="radio" name="radio" />
                        <span class="checkmark" />
                    </label>
                </div>
            </div>

            <div class="des wrapper">
                <p>TELL US MORE</p>
                <textarea name="more" rows="8" cols="80" bind:value={moreDetails} />
            </div>

            <div
                class="generate"
                on:click={() => {
                    fetchImage(generatePrompt(false, false));
                }}
            >
                <p>GENERATE</p>
            </div>
        </div>
    </div>
</div>

<style>
    @font-face {
        font-family: "valko";
        src: url("src/fonts/VALKOCAPELARegular.ttf") format("truetype");
    }
    * {
        font-family: "valko";
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    .body {
        background-color: #45dfa2;
        height: 100vh;
    }
    .grid-container {
        z-index: 5;
        display: grid;
        grid-template-columns: 75vw 25vw;
        grid-template-rows: auto;
        width: 100vw;
        height: 100vh;
    }
    .button:hover {
        cursor: pointer;
    }

    .left {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-column-start: 1;
        grid-column-end: 2;
    }

    .style {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    img {
        margin-top: 8vh;
        width: 30vw;
        height: 80vh;
    }

    .style .button {
        background-color: #eb6468;
        border: 2px solid black;
        border-radius: 10px;
        text-decoration: none;
        color: white;
        padding: 2vw;
        width: 18vw;
        font-size: 25px;
        border-radius: 30;
        margin: 30px;
        margin-left: 50px;
    }

    .placeholder img {
        width: 28vw;
    }

    .placeholder {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .right {
        padding: 0 1vw;
        height: 100vh;
        background-color: white;
        z-index: 5;
        border: 2px solid black;
    }

    /* .wrapper {
        margin: 30px;
    } */

    .wrapper p {
        font-size: 1rem;
        font-weight: 500;
    }

    .wrapper textarea {
        border: 2px solid black;
        border-radius: 10px;
        width: 100%;
        height: 15vw;
    }

    .title {
        font-size: 1.5rem;
    }

    .right .title {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 5vh;
    }

    .container {
        overflow: hidden;
        width: 15vw;
        border: 2px solid black;
        cursor: pointer;
        margin: 1vw 2vw;
        border-radius: 10px;
        padding: 1em;
        text-align: center;
    }

    .container label {
        width: 6vw;
    }

    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .button-container > * {
        text-align: center;
    }

    .button-container .active {
        background-color: black;
        color: white;
    }

    .container input {
        position: absolute;
        opacity: 0;
        cursor: pointer;
    }

    .generate p {
        text-align: center;
        background-color: #4cf2b0;
        overflow: hidden;
        width: 12vw;
        border: 2px solid black;
        cursor: pointer;
        margin: 1vw 2vw;
        border-radius: 10px;
        /* padding: 15px; */
        text-align: center;
    }

    .right .generate {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .loader {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: row;
        position: absolute;
    }

    .slider {
        overflow: hidden;
        background-color: white;
        margin: 0 0.5vw;
        height: 3.5vw;
        width: 1vw;
        border-radius: 30px;
        border-radius: 30px;
        box-shadow: 15px 15px 20px rgba(0, 0, 0, 0.1), -15px -15px 30px #fff,
            inset -5px -5px 10px rgba(0, 0, 255, 0.1), inset 5px 5px 10px rgba(0, 0, 0, 0.1);
        position: relative;
    }

    .slider::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        height: 20px;
        width: 20px;
        border-radius: 100%;
        box-shadow: inset 0px 0px 0px rgba(0, 0, 0, 0.3), 0px 420px 0 400px #2697f3,
            inset 0px 0px 0px rgba(0, 0, 0, 0.1);
        animation: animate_2 2.5s ease-in-out infinite;
        animation-delay: calc(-0.5s * var(--i));
    }

    @keyframes animate_2 {
        0% {
            transform: translateY(250px);
            filter: hue-rotate(100deg);
        }

        50% {
            transform: translateY(0);
        }

        100% {
            transform: translateY(250px);
            filter: hue-rotate(180deg);
        }
    }

    .blur {
        filter: blur(4px);
    }
</style>
