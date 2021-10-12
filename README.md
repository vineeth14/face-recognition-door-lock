# face-recognition-door-lock

This Project works using Raspberry Pi Camera to capture the image of the person at the door if the button is pressed and after that, the image is sent to AWS Rekognition Service for recognition of the face of the person with the authorized user’s faces and if the face is recognized successfully then the electronic door lock connected to Raspberry Pi is Unlocked for the authorized user to enter in the room.

In case if the person is not recognized then the image f that person is sent to the authorized user’s email address.

With the use of AWS Rekognition service, the processing of the image for face recognition is faster as well as accurate and this makes the project fast, reliable, cheap as well as highly secured as compared to other existing projects.

This development scheme using Raspberry Pi is less power consumption as it can be also powered by a power bank or 5V power supply and flexible as the size of Raspberry Pi is compact so it can be installed in a small space.
