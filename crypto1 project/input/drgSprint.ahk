#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#MaxThreads 50
#MenuMaskKey vk07
 
 
 
 
 
;Find and replace the following with your prefered button layout. All of them have to be set to a VALID button:
;LShift = Hold to walk. Alternatively toggles sprinting (see below). Default: 'LShift'
;f7 = The button you assign sprint to in Deep rock. Default: 'f7'
;LButton = Pew Pew! Default: 'LButton'
;RButton = The button that makes you smash rocks. Default: 'RButton'
;LAlt = To activate the "dash" active perk. Default: 'LAlt'
;f6 = Toggles the script on and off
 
f6::
suspend
return
 
 
#IfWinActive, Deep Rock Galactic
 
shooting := 0
sprinting := false
 
 
 
 
;Depending on your preference choose the behaviour of the WALK button (default 'LShift'). Uncomment the block you want, comment the one you don't want. By default the "Sprint Toggle" block is commented.
 
 
;Sprint toggle {
 
;~LShift::
;sprinting := !(sprinting)
;If (sprinting){
;   Send {f7 Down}
;   shooting := 0
;} else
;   Send {f7 Up}
;return
 
;------------- }
 
;Hold to Walk {
 
~LShift::
sprinting := false
Send {f7 Up}
shooting := 0
return
 
~LShift up::
sprinting := true
If (shooting = 0){
    Send {f7 Down}
}
return
 
;-------------- }
 
 
 
 
~LAlt::
send {f7}{f7}
if (sprinting)
    send {f7 down}
else
    send {f7 up}
return
 
#If (sprinting and WinActive("Deep Rock Galactic"))
 
~esc::
Sleep, 100
if(sprinting){
    Send {f7 up}
    Send {f7 down}
}
return
 
#MaxThreadsPerHotkey 40
~LButton::
~RButton::
shooting := shooting + 1
Send {f7 Up}
return
 
 
~LButton up::       ;Shooting
~RButton up::       ;Mining
Sleep, 250      ;Delay before dwarf starts sprinting again (ms). Prevents some issues with burst fire patterns. Adjust up or down according to personal preference and weapon usage.
If(shooting > 0){
    shooting := shooting - 1
}
 
If (sprinting  && (shooting = 0)){
    Send {f7 Down}
}
return
