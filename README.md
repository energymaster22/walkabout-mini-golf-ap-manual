# Walkabout Mini Golf AP Manual
Manual Archipelago randomizer implementation for Walkabout Mini Golf

Walkabout Mini Golf is a VR mini golf game where you putt through various lands and locales while finding collectable lost balls and special fox hunt clues to collect special putters along the way! The game is on most VR platforms and has recently released a "Pocket Edition" on iOS to play on the go!

## Setup:
Create a new profile from the profiles screen to the right of the course select in the shack (Skip if you are on mobile)  (Remember to change your settings to what you like as all settings are per profile)

## Checks:
+ Each individual hole (1 - 18) on both easy and hard variants of selected courses
+ All 18 lost balls on the easy variant of selected courses
+ Each individual fox hunt clue on the hard variant of selected courses
+ All 31 practice holes at The Shack
+ 8 Targets at the driving range of The Shack

## Items:
+ Course unlocks: Lets you enter the easy variant of the course (start with one random course)
+ Progressive stroke limit: By default you are only allowed one stroke per hole! Collecting Progressive stroke limits allows you to take one more shot on each hole per item (Progressive stroke limit is strictly for the course and difficulty that it says in the item name)
+ Lost Balls: Requires 10 of a holes lost balls to enter the hard variant of the course
+ Putters: Currently not useful
+ Score cards: (Not randomized) Used to track which courses you have completed

## Win Condition:
Currently there is only one clear condition which is completing all the courses across easy and hard. After you complete each course, go to the "Course Completion" category to mark your completion and claim your score card for the course. Once you have all your score cards you can claim victory!

## Variants:
Currently we have two variants of the manual with slightly different logic:
+ Energymaster's variant expects you to do all the holes in order and be able to complete each hole before moving on to the next. This variant is best played in the normal play mode, resetting the course from the settings screen if you go over your stroke limit. Forfeiting holes that are already completed or checked via collect is optional.
+ MusicBlox's variant lets you do any hole in any order as long as you have access to the course. This variant is best played in the practice mode so you can move around different holes freely. Selecting the holes from the score card or from the god view will put your ball down on the tee of the chosen hole. One limitation of practice is you will need to keep track of your current stroke count in your head, as the practice mode does not have a stroke counter. If playing this variant you may want to go into your chosen courses and get under par on the easy variant of the course to unlock the hard in advance, as you may want to head into the hard before you grab lost balls or play the easy, you do still need the lost ball items and the easy course unlock to enter the hard.

## Notes:
+ If playing on mobile, due to limitations of this version, you can simply send out all of the lost ball or fox hunt checks once you gain access to the course as this version does not let you create additional profiles to "recollect" the lost balls, nor does it have fox hunts as of writing due to limitations with the mobile versions movement. The same applies to the practice hole checks and the driving range checks for The Shack.
+ You are logically expected to have stroke limit up to par to complete a hole, however, if you feel you can get under that (or even hole in one) enjoy getting checks out of logic!
+ If playing on PCVR I recommend having a VR overlay such as OVR Toolkit, XSOverlay, or Desktop+ to monitor the multiworld and view your manual client easier!

Currently the manual only contains the first two courses in the game being Tourist Trap and Cherry Blossom, however once we figure out yaml options we will be adding the rest of the courses so you will be able to adjust which courses you do and don't want to play and/or own in the case of DLC courses.
