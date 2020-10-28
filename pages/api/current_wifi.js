async function isLocal (ip) {
    ip = ip
    url = `http://${ip}:4005/home/pi/glimpse-cam/`;
    
    const alive = await fetch(url, {
      method: 'GET',
      mode: 'no-cors',
      headers: {
          'Content-Type': 'application/json'
      },
    });
  

    const response = await alive.status;
    if (response == 0){
      
      console.log("on same network")
      return true;

    }
    else{
      errorElement.innerText = "not on same network";
      console.log("not on same network")
      return false;
    }
