---
title: "Copy Components With Mates to Assembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Components_With_Mates_To_Assembly_Example_VBNET.htm"
---

# Copy Components With Mates to Assembly Example (VB.NET)

This example shows how to copy components with mates in an assembly.

'---------------------------------------------------------------------------- ' Preconditions: ' 1. Open public_documents \samples\tutorial\driveworksxpress\mobile gantry.SLDASM . ' 2. Inspect Leg<1> and Leg<2> in the assembly. ' ' Postconditions: ' 1. Replaces Leg<1> with a copy of Leg<2> . ' 2. Inspect Leg<2> and leg<3> in the assembly. ' ' NOTE: Because this assembly is used elsewhere, do not save changes. '----------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks

Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelDocExt As ModelDocExtension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgr As SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
blRepeat(2) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
blFlip(2) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelectedComps As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
RepeatOptions As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
MateRefs As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
InpValues As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
FlipValues As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAssy As AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swItem As Component

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swFeature As Feature

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
refPlane As RefPlane

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
arrMateEntities(2) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
arrCompsToCopy(0) As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dValues(2) As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAssy
= swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelMgr
= swModel.**SelectionManager**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModelDocExt
= swModel.**Extension**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.**SelectByID2**("Leg-1@mobile gantry", "COMPONENT",
0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.**EditDelete**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.**ClearSelection2**(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.**SelectByID2**("Leg-2@mobile gantry", "COMPONENT",
0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swItem
= CType(swSelMgr.**GetSelectedObject6**(1, -1), Component2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}arrCompsToCopy(0)
= swItem

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}arrMateEntities(0)
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}arrMateEntities(1)
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.**SelectByID2**("Left End@Universal Beam-1@mobile gantry",
"PLANE", 0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swFeature
= CType(swSelMgr.**GetSelectedObject6**(1, -1), Feature)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}refPlane
= CType(swFeature.**GetSpecificFeature2**, RefPlane)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}arrMateEntities(2)
= refPlane

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.**ClearSelection2**(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blRepeat(0)
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blRepeat(1)
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blRepeat(2)
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectedComps
= arrCompsToCopy

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RepeatOptions
= blRepeat

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MateRefs
= arrMateEntities

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dValues(0)
= 0.0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dValues(1)
= 0.0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dValues(2)
= 0.0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}InpValues
= dValues

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blFlip(0)
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blFlip(1)
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}blFlip(2)
= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FlipValues
= blFlip

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
disparrCompsToCopy(0) As DispatchWrapper

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}disparrCompsToCopy(0)
= New DispatchWrapper(arrCompsToCopy(0))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
dispMateRefs(2) As DispatchWrapper

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dispMateRefs(0)
= New DispatchWrapper(MateRefs(0))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dispMateRefs(1)
= New DispatchWrapper(MateRefs(1))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dispMateRefs(2)
= New DispatchWrapper(MateRefs(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Repeat
all mates except the coincident mate with "Right End@Universal Beam-1"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAssy.CopyWithMates((disparrCompsToCopy),
RepeatOptions, (dispMateRefs), InpValues, FlipValues)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swAssy.**EditRebuild**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
