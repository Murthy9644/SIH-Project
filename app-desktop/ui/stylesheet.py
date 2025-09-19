sheet = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trip Pilot</title>
    <link href="https://fonts.googleapis.com/css?family=Poppins:400,500,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css">
	<style>
		/* Animations */
		@keyframes slideDown {
		    0%{
		        top: 0px;
		        opacity: 0;
		    }
		    100%{
		        top: 20px;
		        opacity: 1;
		    }
		}
		
		body{
		    padding: 0;
		    margin: 0;
		    background: linear-gradient(to bottom right, rgb(25, 169, 226), rgb(25, 72, 226), rgb(25, 169, 226));
		    font-family: 'Poppins', Arial, sans-serif;
		}
		
		#temp{
		    height: 100vh;
		    width: 100vw;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    flex-direction: column;
		}
		
		#alert{
		    width: 300px;
		    height: 150px;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    flex-direction: column;
		    background-color: rgb(255, 255, 255);
		    border-radius: 10px;
		    padding: 20px;
		    color: red;
		    position: fixed;
		    left: 50%;
		    transform: translate(-50%, 0%);
		    filter: drop-shadow(1px 1px 20px rgba(0, 0, 0, 0.5));
		    z-index: 999;
		    font-size: 16px;
		    animation: slideDown 0.2s forwards;
		}
		
		#alert button{
		    width: 40px;
		    border: none;
		    background-color: blue;
		    padding: 5px;
		    border-radius: 8px;
		    color: white;
		}
		
		
		/* Login Screen */
		
		#login-screen{
		    height: 100vh;
		    width: 100vw;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		}
		
		#login-screen-child{
		    height: 80%;
		    width: 100%;
		    display: flex;
		    align-items: center;
		    justify-content: space-evenly;
		    flex-direction: column;
		}
		
		#reg-btn{
		    height: 30px;
		    width: 95%;
		    display: flex;
		    align-items: center;
		    justify-content: right;
		    padding-right: 20px;
		}#reg-btn button{
		    background-color: rgba(255, 255, 255, 0.2);
		    height: 30px;
		    width: 80px;
		    border: none;
		    border-radius: 8px;
		    color: white;
		    font-size: 12px;
		    filter: drop-shadow(0px 0px 10px rgba(0, 0, 0, 0.5));
		}#reg-btn button:hover{
		    color: rgba(255, 255, 255, 0.7);
		}
		
		#login-header{
		    height: 170px;
		    width: auto;
		    display: flex;
		    flex-direction: column;
		    align-items: center;
		    justify-content: center;
		}
		
		#login-header-shield{
		    height: 50px;
		    width: 50px;
		    color: white;
		    border-radius: 50%;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    font-size: 25px;
		    background-color: rgba(255, 255, 255, 0.2);
		    position: relative;
		    top: 15px;
		    filter: drop-shadow(1px 1px 8px rgba(0, 0, 0, 0.3));
		}
		
		#login-header-text{
		    color: white;
		    display: flex;
		    flex-direction: column;
		    align-items: center;
		    justify-content: center;
		    position: relative;
		    top: 5px;
		}
		
		#login-h2{
		    letter-spacing: 0.8px;
		}
		
		#login-p1{
		    position: relative;
		    top: -30px;
		    font-size: 14px;
		    color: rgba(255, 255, 255, 0.8);
		}
		
		#login-container{
		    background-color: white;
		    height: 360px;
		    width: 380px;
		    padding: 25px;
		    border-radius: 8px;
		    display: flex;
		    flex-direction: column;
		    justify-content: center;
		    gap: 5px;
		    filter: drop-shadow(1px 1px 15px rgba(0, 0, 0, 0.3));
		}
		
		#login-container-header{
		    height: auto;
		    width: auto;
		    display: flex;
		    flex-direction: column;
		    align-items: center;
		    justify-content: space-around;
		    line-height: 0px;
		}#login-container-header p{
		    font-size: 13px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#loginId, #loginPswd{
		    display: flex;
		    flex-direction: column;
		    line-height: 0px;
		}
		
		#login-input-container{
		    height: 40px;
		    width: auto;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		}#login-screen-child input{
		    height: 30px;
		    width: 100%;
		    font-size: 12px;
		    border: 1px solid rgba(0, 0, 0, 0.1);
		    background-color: rgba(157, 157, 201, 0.2);
		    border-radius: 8px;
		    padding-left: 10px;
		    position: relative;
		    top: -8px;
		}#login-screen-child input:focus{
		    outline: 2px solid rgb(25, 169, 226);
		}
		
		#captcha{
		    display: flex;
		    align-items: center;
		    justify-content: space-between;
		    padding-top: 10px;
		    height: 50px;
		    position: relative;
		}#text{
		    text-align: center;
		    letter-spacing: 3px;
		    line-height: 0px;
		    height: 30px;
		    width: 50%;
		    background-color: rgba(0, 0, 0, 0.1);
		    position: relative;
		    bottom: 10px;
		}
		
		#login-btn{
		    border: none;
		    border-radius: 6px;
		    height: 40px;
		    background-color: rgb(25, 169, 226);
		    color: white;
		}#login-btn:hover{
		    background-color: rgb(23, 136, 177);
		}#login-btn:focus{
		    outline: 1px solid black;
		}
		
		
		/* Details Form Screen */
		
		#details-screen{
		    display: flex;
		    flex-direction: column;
		    width: 100vw;
		    height: 100vh;
		}
		
		#details-header{
		    display: flex;
		    width: auto;
		    gap: 25%;
		    padding-left: 110px;
		}
		
		#details-back-btn{
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    gap: 5px;
		    width: 120px;
		    height: 30px;
		    border: 0.5px solid rgba(0, 0, 0, 0.1);
		    background-color: transparent;
		    border-radius: 5px;
		    position: relative;
		    top: 30px;
		    left: 20px;
		}#details-back-btn:focus{
		    background-color: rgb(25, 169, 226);
		    color: white;
		}
		
		#details-back-btn i{
		    font-size: 10px;
		}
		
		#details-back-btn p{
		    font-size: 12px;
		}
		
		#details-header-text{
		    display: flex;
		    flex-direction: column;
		    height: 90px;
		    line-height: 0px;
		    align-items: center;
		    justify-content: center;
		}
		
		#details-header-text p{
		    font-size: 14px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#details-form-container{
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    gap: 25px;
		}
		
		#details-personal-information, #details-travel-information{
		    background-color: white;
		    width: 500px;
		    height: 550px;
		    display: flex;
		    flex-direction: column;
		    padding: 20px;
		    border-radius: 8px;
		    gap: 10px;
		}
		
		#details-PI-header, #details-TI-header{
		    display: flex;
		    flex-direction: column;
		    line-height: 0px;
		}
		
		#details-PI-header div, #details-TI-header div{
		    display: flex;
		    align-items: center;
		    gap: 5px;
		    line-height: 0px;
		}
		
		#details-PI-header div i, #details-TI-header div i{
		    color: rgb(16, 201, 201);
		}
		
		#details-PI-header p, #details-TI-header p{
		    font-size: 14px;
		    color: rgba(0, 0, 0, 0.6);
		}
		
		#details-name{
		    display: flex;
		    flex-direction: column;
		    justify-content: center;
		    line-height: 0px;
		}
		
		#details-form-container input{
		    height: 30px;
		    width: 98%;
		    font-size: 12px;
		    border: 1px solid rgba(0, 0, 0, 0.1);
		    background-color: rgba(157, 157, 201, 0.2);
		    border-radius: 8px;
		    padding-left: 10px;
		}#details-form-container input:focus{
		    outline: 2px solid rgb(25, 169, 226);
		}
		
		#details-personal-information div, #details-travel-information div{
		    line-height: 0px;;
		}
		
		#details-foot-buttons{
		    display: flex;
		    justify-content: right;
		    align-items: center;
		    padding-top: 30px;
		    position: relative;
		    right: 126px;
		    gap: 10px;
		}
		
		#details-foot-buttons button{
		    border-radius: 5px;
		    height: 30px;
		    padding: 10px;
		    border: none;
		    display: flex;
		    align-items: center;
		}
		
		#cancelBtn{
		    background-color: transparent;
		}#cancelBtn:focus{
		    background-color: red;
		    color: white;
		}
		
		#generateBtn{
		    background-color: rgb(25, 169, 226);
		    color: white;
		}#generateBtn:hover{
		    background-color: rgb(23, 136, 177);
		}#generateBtn:focus{
		    outline: 1px solid black;
		}
		
		
		/* QR Screen */
		
		#qrScreen{
		    display: flex;
		    align-items: center;
		    justify-content: space-evenly;
		    flex-direction: column;
		    height: 100vh;
		    width: auto;
		}
		
		#qr-header{
		    height: auto;
		    width: 100%;
		    display: flex;
		    align-items: center;
		    justify-content: space-around;
		    line-height: 0;
		}
		
		#qr-header-text{
		    height: 80px;
		    display: flex;
		    flex-direction: column;
		    justify-content: space-around;
		}
		
		#qr-header-text p{
		    font-size: 13px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#qr-header-btns{
		    height: 40px;
		    width: 360px;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    gap: 8px;
		}
		
		#qr-header-btns button{
		    border: 0.5px solid rgba(0, 0, 0, 0.1);
		    border-radius: 5px;
		    height: 40px;
		    width: 120px;
		}
		
		#back-btn{
		    background-color: transparent;
		}
		
		#New-reg-btn{
		    background-color: rgb(25, 169, 226);
		    color: white;
		}
		
		#qr-details-container{
		    width: 100%;
		    display: flex;
		    justify-content: center;
		    gap: 50px;
		}
		
		#qr-code-container, #qr-tid-details-container{
		    width: 450px;
		    background-color: white;
		    padding: 30px;
		    display: flex;
		    align-items: center;
		    justify-content: space-evenly;
		    flex-direction: column;
		    gap: 10px;
		    border-radius: 8px;
		    filter: drop-shadow(1px 1px 8px rgba(0, 0, 0, 0.1));
		}
		
		#qr-tid-details-container{
		    gap: 25px;
		}
		
		#qr-code-header{
		    display: flex;
		    flex-direction: column;
		    line-height: 0;
		    align-items: center;
		    justify-content: center;
		    line-height: 0;
		}
		
		#qr-code-header p{
		    font-size: 13px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#qr-code-image{
		    width: 250px;
		    height: 270px;
		    background-color: white;
		    filter: drop-shadow(1px 1px 15px rgba(0, 0, 0, 0.3));
		    border-radius: 8px;
		}
		
		#qr-bottom-text{
		    display: flex;
		    flex-direction: column;
		    line-height: 0;
		    align-items: center;
		    justify-content: center;
		}
		
		#qr-bottom-text p{
		    font-size: 13px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#tid-header{
		    display: flex;
		    flex-direction: column;
		    justify-content: center;
		    line-height: 0;
		    width: 100%;
		}
		
		#tid-header p{
		    font-size: 13px;
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#tid-number{
		    display: flex;
		    flex-direction: column;
		    line-height: 0;
		    width: 100%;
		}
		
		#number-container{
		    height: 50px;
		    width: 100%;
		    display: flex;
		    align-items: center;
		    gap: 5px;
		}
		
		#number{
		    height: 40px;
		    width: 100%;
		    background-color: rgba(70, 70, 238, 0.3);
		    color: darkblue;
		    font-weight: 600;
		    display: flex;
		    align-items: center;
		    justify-content: left;
		    padding-left: 10px;
		    letter-spacing: 2px;
		    border-radius: 8px;
		}
		
		#copy-btn{
		    height: 35px;
		    width: 40px;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    font-size: 16px;
		    background-color: rgba(185, 184, 184, 0.3);
		    border: none;
		    border-radius: 8px;
		    color: rgb(112, 112, 112);
		}#copy-btn:active{
		    background-color: greenyellow;
		}
		
		#qrScreem:focus{
		    outline: 1px solid black;
		}
		
		#tourist-details{
		    width: 100%;
		}
		
		#tourist-details div{
		    display: flex;
		    align-items: center;
		    justify-content: space-between;
		    line-height: 0;
		}
		
		#tourist-details p{
		    font-size: 13px;
		    font-weight: 600;
		}
		
		#field-name{
		    color: rgba(0, 0, 0, 0.5);
		}
		
		#bottom-btns{
		    height: 50px;
		    width: 100%;
		    display: flex;
		    align-items: center;
		    justify-content: center;
		    gap: 15px;
		}
		
		#bottom-btns button{
		    border: 0.5px solid rgba(0, 0, 0, 0.1);
		    border-radius: 8px;
		    height: 35px;
		    width: auto;
		    padding-left: 20px;
		    padding-right: 20px;
		}
		
		#qrScreen button:focus{
		    outline: 1px solid black;
		}
		
		
		/* Responsive adjustments */
		@media (max-width: 600px) {
		  #login-container {
		    width: 100vw;
		    max-width: 100vw;
		    min-width: 0;
		    height: auto;
		    padding: 10px;
		    margin: 0 auto;
		    box-sizing: border-box;
		    border-radius: 8px;
		  }
		  #login-header {
		    width: 100vw;
		    min-width: unset;
		    max-width: 100vw;
		    height: auto;
		    padding: 10px 0;
		  }
		  #login-screen-child {
		    width: 100vw;
		    height: 100vh;
		    padding: 0;
		  }
		  #login-input-container {
		    width: 100%;
		    min-width: unset;
		    max-width: 100vw;
		  }
		  #captcha {
		    flex-direction: column;
		    height: auto;
		    gap: 10px;
		  }
		  #text {
		    width: 100%;
		    min-width: unset;
		    max-width: 100vw;
		  }
		}
		
		@media (max-width: 400px) {
		  #login-container {
		    width: 98vw;
		    max-width: 98vw;
		    min-width: 0;
		    padding: 5px;
		    margin: 0 auto;
		    box-sizing: border-box;
		    border-radius: 8px;
		  }
		  #login-header {
		    padding: 5px 0;
		  }
		}

	</style></head>

<body id = "body">
    <div id="alertBox"></div>

    <div id="login-screen">
        <div id = "login-screen-child">
            <div id="reg-btn"><button>Register</button></div>
            
            <div id="login-header">
                <div id="login-header-shield">
                    <i class="fa-solid fa-shield"></i>
                </div>
                
                <div id="login-header-text">
                    <h2 id="login-h2">Tourist Safety System</h2>
                    <p id="login-p1">Authorized Personnel Access Only</p>
                </div>
            </div>
            
            <div id="login-container">
                <div id="login-container-header">
                    <h3>Authority Login</h3>
                    <p>Enter your authorized credentials to access the system</p>
                </div>
                
                <div id="loginId">
                    <h5>Authorized ID Number</h5>
                    <div id = "login-input-container">
                        <input id = "login-id-input" type="text" name = "id" placeholder="Enter your ID">
                        <div></div>
                    </div>
                </div>
                
                <div id="loginPswd">
                    <h5>Password</h5>
                    <div id = "login-input-container">
                        <input id = "login-pswd-input" type="password" name = "password" placeholder="Enter your password">
                        <div></div>
                    </div>
                </div>
                
                <div id="captcha">
                    <div id="text"><h3>demo text</h3></div>
                    <div id = "login-input-container">
                        <input type="text" name = "captcha" placeholder="Enter the captcha">
                        <div></div>
                    </div>
                </div>
                
                <button onclick="handleChangeScreen('loginScreen', 'detailsScreen')" id = "login-btn">Login</button>
            </div>
        </div>
    </div>

	<script>
		// Animations
		
		// Global variables
		let tid = ""
		let detailsData = {}
		
		// HTML structure for login screen
		let loginScreenHTML = `
		    <div id="alertBox"></div>
		
		    <div id="login-screen">
		        <div id = "login-screen-child">
		            <div id="reg-btn"><button>Register</button></div>
		            
		            <div id="login-header">
		                <div id="login-header-shield">
		                    <i class="fa-solid fa-shield"></i>
		                </div>
		                
		                <div id="login-header-text">
		                    <h2 id="login-h2">Tourist Safety System</h2>
		                    <p id="login-p1">Authorized Personnel Access Only</p>
		                </div>
		            </div>
		            
		            <div id="login-container">
		                <div id="login-container-header">
		                    <h3>Authority Login</h3>
		                    <p>Enter your authorized credentials to access the system</p>
		                </div>
		                
		                <div id="loginId">
		                    <h5>Authorized ID Number</h5>
		                    <div id = "login-input-container">
		                        <input id = "login-id-input" type="text" name = "id" placeholder="Enter your ID">
		                        <div></div>
		                    </div>
		                </div>
		                
		                <div id="loginPswd">
		                    <h5>Password</h5>
		                    <div id = "login-input-container">
		                        <input id = "login-pswd-input" type="password" name = "password" placeholder="Enter your password">
		                        <div></div>
		                    </div>
		                </div>
		                
		                <div id="captcha">
		                    <div id="text"><h3>demo text</h3></div>
		                    <div id = "login-input-container">
		                        <input type="text" name = "captcha" placeholder="Enter the captcha">
		                        <div></div>
		                    </div>
		                </div>
		                
		                <button onclick="handleChangeScreen('loginScreen', 'detailsScreen')" id = "login-btn">Login</button>
		            </div>
		        </div>
		    </div>
		`
		
		// HTML structure for details screen
		let detailsScreenHTML = `
		    <div id="alertBox"></div>
		
		    <div id="details-screen">
		        <div id="details-header">
		            <button id="details-back-btn" onclick = "changePage('loginScreen', true)">
		                <i class="fa-solid fa-arrow-left"></i>
		                <p>Back to Login</p>
		            </button>
		    
		            <div id="details-header-text">
		                <h2>Tourist Registration</h2>
		                <p>Enter tourist details for safety monitoring</p>
		            </div>
		        </div>
		    
		        <div id="details-form-container">
		            <div id="details-personal-information">
		                <div id="details-PI-header">
		                    <div>
		                        <i class="fa-regular fa-user"></i>
		                        <h3>Personal Information</h3>
		                    </div>
		    
		                    <p>Basic details as per official documentations</p>
		                </div>
		    
		                <div id="details-name">
		                    <h5>Full Name *</h5>
		                    <input type="text" name = "fullname" placeholder="Enter full name">
		                </div>
		    
		                <div id="details-phoneNum">
		                    <h5>Phone Number *</h5>
		                    <input type="tel" name = "phoneNo" placeholder="+1234567890">
		                </div>
		    
		                <div id="details-dob">
		                    <h5>Date of Birth *</h5>
		                    <input type="date" name = dob>
		                </div>
		    
		                <div id="nation">
		                    <h5>Nationality</h5>
		                    <input type="text" placeholder="Enter nationality" name = "nation">
		                </div>
		            </div>
		    
		            <div id="details-travel-information">
		                <div id="details-TI-header">
		                    <div>
		                        <i class="fa-solid fa-location-dot"></i>
		                        <h3>Travel Information</h3>
		                    </div>
		    
		                    <p>Trip details and emergency contacts</p>
		                </div>
		    
		                <div id="details-destination">
		                    <h5>Destination</h5>
		                    <input type="text" placeholder="Enter travel destination" name = "destination">
		                </div>
		    
		                <div id="details-trip-duration">
		                    <h5>Trip Duration *</h5>
		                    <h6>From</h6>
		                    <input type="date" name = "trip-from-date">
		                    <h6>To</h6>
		                    <input type="date" name = "trip-to-date">
		                </div>
		    
		                <div id="details-trip-reason">
		                    <h5>Trip Reason *</h5>
		                    <input type="text" placeholder="Enter the trip reason" name = "tripReason">
		                </div>
		    
		                <div id="details-emergency-contact">
		                    <h5>Emergency Contact</h5>
		                    <input type="tel" placeholder="Emergency contact number" name = emergencyPhn>
		                </div>
		            </div>
		        </div>
		    
		        <div id="details-foot-buttons">
		            <button id = cancelBtn>Cancel</button>
		            <button id = generateBtn onclick = "handleDetails2QR()">Generate QR & Travel ID</button>
		        </div>
		    </div>
		`
		
		let qrScreenHTML = `
		        <div id="qrScreen">
		        <div id="qr-header">
		            <div id="qr-header-text">
		                <h2>Tourist Registration Complete</h2>
		
		                <p>QR Code & Travel ID generated successfully</p>
		            </div>
		
		            <div id="qr-header-btns">
		                <button id = "back-btn"><i class="fa-solid fa-arrow-left" style="font-size: 10px; position: relative; top: -1px;"></i> Back to Form</button>
		                <button id = "New-reg-btn">New Registration</button>
		            </div>
		        </div>
		
		        <div id="qr-details-container">
		            <div id="qr-code-container">
		                <div id="qr-code-header">
		                    <h3><i class="fa-solid fa-qrcode" style="color: rgb(94, 94, 252);"></i> Generated QR Code</h3>
		
		                    <p>Scan this QR code to access the mobile application</p>
		                </div>
		
		                <div id="qr-code-image">
		
		                </div>
		
		                <div id="qr-bottom-text">
		                    <p>This QR code contains encrypted tourist data</p>
		                    <p>for sceure access to the mobile application</p>
		                </div>
		            </div>
		
		            <div id="qr-tid-details-container">
		                <div id="tid-header">
		                    <h3><i class="fa-regular fa-square-check" style="color: rgb(4, 219, 4); font-size: 20px;"></i> Travel ID Generated</h3>
		                    
		                    <p>Unique identifier for this tourist registration</p>
		                </div>
		
		                <div id="tid-number">
		                    <h5>Travel ID</h5>
		
		                    <div id="number-container">
		                        <div id="number"></div>
		
		                        <button id="copy-btn"><i class="fa-solid fa-clone"></i></button>
		                    </div>
		                </div>
		
		                <div id="tourist-details">
		                    <h5>Tourist Information</h5>
		
		                    <div>
		                        <p id="field-name">Name:</p>
		                        <p id="value"></p>
		                    </div>
		
		                    <div>
		                        <p id="field-name">Phone:</p>
		                        <p id="value"></p>
		                    </div>
		
		                    <div>
		                        <p id="field-name">Destination:</p>
		                        <p id="value"></p>
		                    </div>
		
		                    <div>
		                        <p id="field-name">Duration:</p>
		                        <p id="value"></p>
		                    </div>
		
		                    <div>
		                        <p id="field-name">Registration:</p>
		                        <p id="value"></p>
		                    </div>
		                </div>
		            </div>
		        </div>
		
		        <div id="bottom-btns">
		            <button id="download"><i class="fa-solid fa-download"></i> Download PDF</button>
		
		            <button id="print"><i class="fa-solid fa-print"></i> Print</button>
		        </div>
		    </div>
		`
		
		
		// Handles Screen change based on credential check
		async function handleChangeScreen(currentpage, nextpage){
		    
		    let credCheckStatus = await loginCredCheck(currentpage)
		    
		    if (credCheckStatus){
		        changePage(nextpage, true)
		    }
		}
		
		// Handles closing the alert box
		function closeDiv(){
		    document.getElementById("alertBox").innerHTML = ``
		}
		
		// Changes the page based on the given page name
		function changePage(page, credCheckStatus = true){
		
		    if (! credCheckStatus) return
		    
		    switch (page){
		        case "loginScreen":
		                let body = document.getElementById("body")
		                body.style.background = "linear-gradient(to bottom right, rgb(25, 169, 226), rgb(25, 72, 226), rgb(25, 169, 226))"
		                body.style.backgroundColor = "transparent"
		                body.innerHTML = loginScreenHTML
		                break
		
		            case "detailsScreen":
		                let body2 = document.getElementById("body")
		                body2.style.background = "none"
		                body2.style.backgroundColor = "rgba(157, 157, 201, 0.2)"
		                body2.innerHTML = detailsScreenHTML
		                break
		
		            case "qrScreen":
		                let body3 = document.getElementById("body")
		                body3.innerHTML = qrScreenHTML
		                document.getElementById("qr-code-image").innerHTML = `<img src="./assets/qr_codes/${tid}.png" alt="QR Code">`
		                document.getElementById("number").innerText = tid
		                document.getElementById("tourist-details").children[1].children[1].innerText = detailsData["fullname"]
		                document.getElementById("tourist-details").children[2].children[1].innerText = detailsData["phoneNo"]
		                document.getElementById("tourist-details").children[3].children[1].innerText = detailsData["destination"]
		                document.getElementById("tourist-details").children[4].children[1].innerText = `${detailsData["duration"][0]} to ${detailsData["duration"][1]}`
		                document.getElementById("body").style.backgroundColor = "rgba(157, 157, 201, 0.2)"
		                document.getElementById("body").style.background = "none"
		                break
		        }
		}
		
		// Checks if all required credentials are filled before changing the page
		async function loginCredCheck(page){
		
		    switch (page){
		        case "loginScreen":
		            let id = document.querySelector("input[name='id']")
		            let pswd = document.querySelector("input[name='password']")
		            let captcha = document.querySelector('input[name = "captcha"]')
		            
		            let loginData = {
		                id: id ? id.value : '',
		                pswd: pswd ? pswd.value : '',
		                captcha: captcha ? captcha.value : ''
		            }
		
		            let response = await window.pywebview.api.widutils.credCheck(loginData, page)
		            
		            if (! response){
		                document.getElementById("alertBox").innerHTML = `
		                <div id="alert">
		                    <p>Fill all the required credentials before submitting.</p>
		                    <button onclick="closeDiv()">OK</button>
		                </div>
		                `
		
		                return false
		            }
		
		            break
		
		            case "detailsScreen":
		            let fullname = document.querySelector('input[name = "fullname"]')
		            let phoneNo = document.querySelector('input[name = "phoneNo"]')
		            let dob = document.querySelector('input[name = "dob"]')
		            let tripFromDate = document.querySelector('input[name = "trip-from-date"]')
		            let tripToDate = document.querySelector('input[name = "trip-to-date"]')
		            let tripReason = document.querySelector('input[name = "tripReason"]')
		
		            let detailsData = {
		                fullname: fullname ? fullname.value : '',
		                phoneNo: phoneNo ? phoneNo.value : '',
		                dob: dob ? dob.value : '',
		                tripFromDate: tripFromDate ? tripFromDate.value : '',
		                tripToDate: tripToDate ? tripToDate.value : '',
		                tripReason: tripReason ? tripReason.value : '',
		            }
		
		            let response2 = await window.pywebview.api.widutils.credCheck(detailsData, page)
		            
		            if (! response2){
		                document.getElementById("alertBox").innerHTML = `
		                <div id="alert">
		                    <p>Fill all the required credentials before submitting.</p>
		                    <button onclick="closeDiv()">OK</button>
		                </div>
		                `
		
		                return false
		            }
		
		            break
		            
		            default:
		            break
		        }
		
		        return true
		    }
		//Handles Details to QR code generation
		async function handleDetails2QR(){
		    let credCheckStatus = await loginCredCheck("detailsScreen")
		        
		    if (! credCheckStatus) return
		    
		    document.getElementById("generateBtn").innerText = "Generating QR..."
		    document.getElementById("generateBtn").style.color = "rgba(220, 220, 220, 0.7)"
		    document.getElementById("generateBtn").style.cursor = "not-allowed"
		    document.getElementById("generateBtn").disabled = true
		
		    let tidNo = Date.now()
		    
		    let detailsData = {
		        fullname: document.querySelector('input[name = "fullname"]').value,
		        phoneNo: document.querySelector('input[name = "phoneNo"]').value,
		        dob: document.querySelector('input[name = "dob"]').value,
		        nationality: document.querySelector('input[name = "nation"]').value,
		        destination: document.querySelector('input[name = "destination"]').value,
		        duration: [document.querySelector('input[name = "trip-from-date"]').value, document.querySelector('input[name = "trip-to-date"]').value],
		        tripReason: document.querySelector('input[name = "tripReason"]').value,
		        emergencyContact: document.querySelector('input[name = "emergencyPhn"]').value
		    }
		
		    tid = `${detailsData["fullname"][0]}-${tidNo}`
		    dataTransferStatus = await window.pywebview.api.dataTransfer.sendData(detailsData, tid)
		
		    if (dataTransferStatus == "success") changePage("qrScreen", true)
		
		    document.getElementById("generateBtn").innerText = "Generate QR & Travel ID"
		    document.getElementById("generateBtn").style.color = "white"
		    document.getElementById("generateBtn").style.cursor = "pointer"
		    document.getElementById("generateBtn").disabled = false
		}
	</script>
</body>
</html>
'''