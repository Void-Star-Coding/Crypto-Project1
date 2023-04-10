#singleinstance force
Sendmode Input

#MaxThreads 50



SetBatchLines,-1

shooting := 0
sprinting := false
isSprintingRn:= false
timeToSprint := 0

;AHK only supports single THREAD / 1 LOOP

loop {
	startSprinting := not isAttacking() and wantsToSprint() and not isSprintingRn
	stopSprinting := isSprintingRn and (isAttacking() or not wantsToSprint())
	
	isTimeToSprint := timeToSprint >= 300
	;tooltip, %timeToSprint% `nisSprintingRnstartSprinting %startSprinting% `nisSprintingRn %isSprintingRn% `nstopSprinting %stopSprinting%
	

	if(startSprinting and isTimeToSprint) {
		sprintGo()
	}
		
	if(stopSprinting) {
		sprintStop()
		timeToSprint := 0
	}
	sleepTime := 100
	timeToSprint := timeToSprint + sleepTime
	sleep sleepTime
}

~esc::sprintStop()

[:: reload 
]:: exitapp


waitToSprint() {
	sleep 175
}


sprintGo() {
	;waitToSprint()
	global isSprintingRn := true
	send {lshift down}
}

sprintStop() {
	global isSprintingRn := false
	send {lshift up}
}

isAttacking() {
	return GetKeyState("LButton","P") or GetKeyState("RButton","P")
}

wantsToSprint() {
	return GetKeyState("W","P")
}























