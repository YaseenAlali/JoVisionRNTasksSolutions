import { StyleSheet, Text, View, Button, Dimensions } from 'react-native';
import { useEffect, useState, useRef, } from 'react';
import { Camera } from 'expo-camera';
import * as MediaLibrary from 'expo-media-library';
import { useIsFocused } from '@react-navigation/core';
const windowWidth = Dimensions.get('window').width;
import * as FileSystem from 'expo-file-system'
export default function TabOneScreen() {
    let cameraRef = useRef();
    const [hasCameraPermission, setHasCameraPermission] = useState();
    const [hasMicrophonePermission, setHasMicrophonePermission] = useState();
    const [hasMediaLibraryPermission, setHasMediaLibraryPermission] = useState();
    const [isRecording, setIsRecording] = useState(false);
    const [video, setVideo] = useState();
    const isFoucsed = useIsFocused();


    function formatISOTimeString(timeString = '') {
        try {
            var charsToRemove = '-TZ.:'
            const regexPattern = `[${charsToRemove}]`;
            const regex = new RegExp(regexPattern, 'g');
            const newString = timeString.replace(regex, '');
            return newString;
        } catch (error) {
            console.warn(`Error in formatting ISO time string ${error}`);
        }
    };

    useEffect(() => {
        (async () => {
            const cameraPermission = await Camera.requestCameraPermissionsAsync();
            const microphonePermission = await Camera.requestMicrophonePermissionsAsync();
            const mediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();

            setHasCameraPermission(cameraPermission.status === "granted");
            setHasMicrophonePermission(microphonePermission.status === "granted");
            setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
        })();
    }, []);

    if (hasCameraPermission === undefined || hasMicrophonePermission === undefined) {
        return <Text>Requestion permissions...</Text>
    } else if (!hasCameraPermission) {
        return <Text>Permission for camera not granted.</Text>
    }

    let recordVideo = () => {
        setIsRecording(true);
        let options = {
            quality: "1080p",
            maxDuration: 60,
            mute: false
        };


        cameraRef.current.recordAsync(options).then((recordedVideo) => {
            let dateIso = formatISOTimeString(new Date().toISOString());
            let newName = `${dateIso}_VID.mp4`;
            if (recordedVideo.uri) {
                let newUri = recordedVideo.uri.replace(recordedVideo.uri.split('/').pop(), newName);
                FileSystem.moveAsync({ from: recordedVideo.uri, to: newUri }).then(() => {
                    console.log(recordedVideo.uri, newUri);
                    recordedVideo.uri = newUri;
                    setVideo(recordedVideo);
                    setIsRecording(false);
                }).catch((error) => {
                    console.warn(error);
                })
            }
        });
    };

    let stopRecording = () => {
        setIsRecording(false);
        cameraRef.current.stopRecording();
    };

    let saveVideo = () => {
        MediaLibrary.saveToLibraryAsync(video.uri).then(() => {
            setVideo(undefined);
        }).catch((error) => {
            console.warn(error);
        })
    };

    if (isFoucsed)
        return (
            <Camera style={styles.container} ref={cameraRef} ratio='16:9'>
                <View style={styles.buttonContainer}>
                    <View style={styles.button}>
                        <Button title={isRecording ? "Stop Recording" : "Record Video"} onPress={isRecording ? stopRecording : recordVideo} />
                    </View>
                    {hasMediaLibraryPermission && video ? (
                        <View style={styles.button}>
                            <Button title="Save" onPress={saveVideo} />
                        </View>
                    ) : null}
                    {video ? (
                        <View style={styles.button}>
                            <Button title="Discard" onPress={() => setVideo(undefined)} />
                        </View>
                    ) : null}
                </View>
            </Camera>
        );
    return undefined;
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    buttonContainer: {
        position: 'absolute',
        bottom: 0,
        width: windowWidth,
        flexDirection: 'row',
        justifyContent: 'center',
        backgroundColor: 'transparent',
        paddingVertical: 10,
    },
    button: {
        flex: 1,
        marginHorizontal: 5,
    },
});