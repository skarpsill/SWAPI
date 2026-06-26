---
title: "Get Blocks Data in Any Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocks_Data_in_Any_Document_Example_VB.htm"
---

# Get Blocks Data in Any Document Example (VBA)

This example shows how to get blocks data in part, assembly, and drawing
documents.

'--------------------------------

'

' Preconditions: Part, assembly, or drawing document containing

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}one
or more block definitions

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}and
block instances is open.

'

' Postconditions: None

'

'---------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim skMgr As SldWorks.SketchManager

Dim pBlock As SldWorks.SketchBlockDefinition

Dim pInst As SldWorks.SketchBlockInstance

Dim leaderPt As SldWorks.MathPoint

Dim insPt As SldWorks.MathPoint

Dim vInstPt As Variant

Dim vInstances As Variant

Dim vBlocks As Variant

Dim nInstanceCount As Long

Dim itr As Long

Dim jtr As Long

Dim bLinkToFile As Boolean

Dim strInsPoint As String

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
skMgr = swModel.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBlocks
= skMgr.GetSketchBlockDefinitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Exit if no blocks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vBlocks) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Process block definitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vBlocks)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pBlock = vBlocks(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block defintion linked to file?

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Link
To File = " & pBlock.LinkToFile

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block linked file name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Link
File Name = " & pBlock.FileName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block definition insertion point

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
insPt = pBlock.InsertionPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vInstPt
= insPt.ArrayData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strInsPoint
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Insertion
point: x = " + CStr(vInstPt(0) * 1000) + " , y = " + CStr(vInstPt(1)
* 1000) + " , z = " + CStr(vInstPt(2) * 1000)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
strInsPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Number of block instances of this block definition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nInstanceCount
= pBlock.GetInstanceCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Instance
Count = " & nInstanceCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Process block instances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
nInstanceCount > 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vInstances
= pBlock.GetInstances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
jtr = 0 To UBound(vInstances)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pInst = vInstances(jtr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block instance position

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
insPt = pInst.InstancePosition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vInstPt
= insPt.ArrayData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}strInsPoint
= "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Instance
position: x = " + CStr(vInstPt(0) * 1000) + " , y = " +
CStr(vInstPt(1) * 1000) + " , z = " + CStr(vInstPt(2) * 1000)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
strInsPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block instance angle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Angle
= " & pInst.Angle

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block instance scale

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Scale
= " & pInst.Scale

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Block instance owner's sketch name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Owner
Sketch = " & pInst.GetSketch.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
jtr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
