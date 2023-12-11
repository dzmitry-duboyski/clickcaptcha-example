![image](https://github.com/dzmitry-duboyski/clickcaptcha-example/assets/38065632/91e26e72-41ca-4c7c-94b7-bdd0c37dcbcc)


# Example for solving clickcaptcha (coordinates) in python

Clickcaptcha (coordinates) is a captcha in which you need to click on the image in accordance with the instructions.
In this example, the captcha located on the page https://2captcha.com/demo/clickcaptcha is solved.

### How does the solution occur in the example?
1. Open the page with the captcha
2. Save the image with the captcha.
3. Submit captcha to [2captcha](https://2captcha.com/) API  to receive a response.
4. Move the cursor to the original coordinates with the captcha, then move the cursor along the received coordinates and click (done three times)
5. Click on the "Check" button to check the result.

