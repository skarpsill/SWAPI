---
title: "Get Block Definitions in Part or Assembly Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Block_Definitions_in_Part_or_Assembly_Example_VB.htm"
---

# Get Block Definitions in Part or Assembly Example (VBA)

This example shows how to get all of the block definitions and their
block instances in a part or assembly.

'-----------------------------

'

' Preconditions: Part document is open and contains at
least

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}one
block definition and block instance.

'

' Postconditions: All of the block instances in the part
are selected.

'

'-----------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim skMgr As SldWorks.SketchManager

Dim swSelMgr As SldWorks.SelectionMgr

Dim selBlockInst As SldWorks.SketchBlockInstance

Dim pBlock As SldWorks.SketchBlockDefinition

Dim pInst As Object

Dim vBlocks As Variant

Dim vInstances As Variant

Dim itr As Long

Dim jtr As Long

Dim retval As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
skMgr = swModel.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBlocks
= skMgr.GetSketchBlockDefinitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Exit if no block definitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
IsEmpty(vBlocks) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Process blocks instances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
itr = 0 To UBound(vBlocks)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pBlock = vBlocks(itr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vInstances
= pBlock.GetInstances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
False = IsEmpty(vInstances) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
jtr = 0 To UBound(vInstances)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pInst = vInstances(jtr)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}retval
= pInst.Select(True, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
selBlockInst = swSelMgr.GetSelectedObject6(1,
-1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
jtr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
itr

End Sub
