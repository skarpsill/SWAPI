---
title: "Get Blocks in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocks_in_Drawing_Example_VB.htm"
---

# Get Blocks in Drawing Example (VBA)

This example shows how to get a block definition and its block instances
in a drawing.

'---------------------------------------------------

'

' Precondition:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Drawing is open that contains at least

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}one
block definition with at least one

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}block
instance.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
The block definition is selected in the

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FeatureManager
design tree.

'

' Postconditions: None

'

'----------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFeat As SldWorks.Feature

Dim swBlockDef As SldWorks.SketchBlockDefinition

Dim swBlockInst As SldWorks.SketchBlockInstance

Dim nbrBlockInst As Integer

Dim vBlockInst As Variant

Dim itr As Integer

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swSelMgr = swModel.SelectionManager

Set swFeat = swSelMgr.GetSelectedObject6(1,
0)

Set swBlockDef = swFeat.GetSpecificFeature2

Debug.Print "Feature type: " & swFeat.GetTypeName

nbrBlockInst = swBlockDef.GetInstanceCount

Debug.Print "Number of instances of selected block:
" & nbrBlockInst

If nbrBlockInst > 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBlockInst
= swBlockDef.GetInstances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To (nbrBlockInst - 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBlockInst = vBlockInst(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Name of block instances: " & swBlockInst.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

End If

End Sub
