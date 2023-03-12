<script>
    import Navbar from "./Navbar.svelte";
</script>

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
    color:white;
}


@keyframes rotate {
  from {
    rotate: 0deg;
  }

  50% {
    scale: 1 1.5;
  }

  to {
    rotate: 360deg;
  }
}

#blob {
  background-color: white;
  height: 34vmax;
  aspect-ratio: 1;
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  border-radius: 50%;
  background: linear-gradient(to right, aquamarine, mediumpurple);
  animation: rotate 20s infinite;
  opacity: 0.8;
}

#blur {
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 2;
  backdrop-filter: blur(12vmax);
}
main {
    position:absolute;
    z-index:3;
    height: 100vh;
}

.title,team-container {
  padding-top: 15vh;

}

.title {
font-size: 60px;
text-align: center;
margin-bottom: 30px;
color:  #45dfa2;

  font-weight: bold;
}
.team-container {
  display: grid;
  grid-template-columns: auto auto auto;
  place-items: center;
  width: 100vw;

}


.ava img{
  width: 20vw;
  min-width: 190px;
  border-radius: 30px;
}

.content {
margin-left: 3vw;
margin-top: 1vh;

}

.name {
font-size: 36px;
}

.role {
font-size: 20px;
}

@media (max-width: 800px) {
.team-container {
  grid-template-columns: auto;
}
}

</style>

<div id="blob"></div>
<div id="blur"></div>
<main>
<Navbar/>

<div class="title">
OUR TEAM
</div>

<div class="team-container">

<div class="team">

  <div class="ava">
<img src="src\assets\quang.png" alt="">
  </div>

  <div class="content">
    <div class="name">
    QUANG
    </div>

    <div class="role">
      Front-end Dev
    </div>

    <div class="des">

    </div>

  </div>

</div>

<div class="team">

  <div class="ava">
<img src="src\assets\phu.png" alt="">
  </div>

  <div class="content">
    <div class="name">
    PHU
    </div>

    <div class="role">
Front-end Dev
    </div>

    <div class="des">

    </div>

  </div>

</div>

<div class="team">

  <div class="ava">
<img src="src\assets\nguyen.png" alt="">
  </div>

  <div class="content">
    <div class="name">
    NGUYEN
    </div>

    <div class="role">
Back-end Dev
    </div>

    <div class="des">

    </div>

  </div>

</div>

</div>



</main>
