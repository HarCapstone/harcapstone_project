import cv2
import time
from flask import Flask, url_for ,render_template, Response

#Initialize Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')      

def gen():
    cap = cv2.VideoCapture('queda.mp4')
    fgbg = cv2.createBackgroundSubtractorMOG2()  # create background subtractor
    j = 0

    while(1):

        ret, frame = cap.read()

  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)

        # Find contours
        contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:

            # List to hold all areas
            areas = []

            for contour in contours:
                ar = cv2.contourArea(contour)
                areas.append(ar)

            max_area = max(areas, default=0)

            max_area_index = areas.index(max_area)

            cnt = contours[max_area_index]

            M = cv2.moments(cnt)

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.drawContours(fgmask, [cnt], 0, (255, 255, 255), 3, maxLevel=0)

            if h < w:
                j += 1

            if j > 10:
                # print("FALL")
                # cv2.putText(fgmask, 'FALL', (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,255,255), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            if h > w:
                j = 0
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
            cv2.imshow('video', frame)
            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            key = cv2.waitKey(20)
            if key == 27:
                return
                

 
        
           

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)


        

