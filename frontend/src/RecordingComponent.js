import React, { useState } from 'react';
import { ReactMic } from 'react-mic';

const RecordingComponent = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [result,setResult] = useState("")

  const onStartRecording = () => {
    setIsRecording(true);
    setResult("")
  };

  const onStopRecording = (recordedBlob) => {
    setIsRecording(false);
    sendAudioToBackend(recordedBlob.blob);
  };

  const sendAudioToBackend = async (audioBlob) => {
    try {
      if (!(audioBlob instanceof Blob)) {
        console.error('The provided audioBlob is not a Blob object:', audioBlob);
        return;
      }
  
      const formData = new FormData();
      formData.append('audio', audioBlob, '16-122828-0002.wav');
  
      // const response = await fetch('http://127.0.0.1:5000/upload-audio', {
      const response = await fetch('http://127.0.0.1:8000/audio_to_text', { 
        method: 'POST',
        body: formData
      });
  
      if (response.ok) {
        setResult("Uploaded successfully")
        console.log(response.body)
      } else {
        console.error('Failed to upload audio:', response.statusText);
      }
    } catch (error) {
      console.error('Error uploading audio:', error);
    }
  };

  return (
    <div>
    <div>
      <ReactMic
        record={isRecording}
        className="sound-wave"
        onStop={onStopRecording}
        strokeColor="#000000"
        backgroundColor="#FF4081"
      />
    </div>
    <div>
      <button onClick={onStartRecording} disabled={isRecording}>
        Start Recording
      </button>
      <button onClick={onStopRecording} disabled={!isRecording}>
        Stop Recording
      </button>
      <p>{result}</p>
    </div>
    </div>
  );
};

export default RecordingComponent;
