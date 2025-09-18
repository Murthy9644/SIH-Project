// Animations

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
                    <h5>Designation</h5>
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
            <button id = generateBtn>Generate QR & Travel ID</button>
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
    }
}

// Checks if all required credentials are filled before changing the page
async function loginCredCheck(page){

    switch (page){
        case "loginScreen":
            let id = document.querySelector("input[name='id']")
            let pswd = document.querySelector("input[name='password']")
            let captcha = document.querySelector('input[name = "captcha"')

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
            let destination = document.querySelector('input[name = "destination"]')
            let tripFromDate = document.querySelector('input[name = "trip-from-date"]')
            let tripToDate = document.querySelector('input[name = "trip-to-date"]')
            let tripReason = document.querySelector('input[name = "tripReason"]')

            let detailsData = {
                fullname: fullname ? fullname.value : '',
                phoneNo: phoneNo ? phoneNo.value : '',
                dob: dob ? dob.value : '',
                destination: destination ? destination.value : '',
                tripFromDate: tripFromDate ? tripFromDate.value : '',
                tripToDate: tripToDate ? tripToDate.value : '',
                tripReason: tripReason ? tripReason.value : '',
                emergencyPhn: emergencyPhn ? emergencyPhn.value : ''
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