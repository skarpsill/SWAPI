---
title: "Make Smart Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Smart_Component_Example_VB.htm"
---

# Make Smart Component Example (VBA)

This example shows how to create a Smart Component.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open an assembly containing three components.
' 2. Change names of the selected components in
'    the macro to match the names of the components
'    in your assembly.
'
' Postconditions:
' 1. Creates a Smart Component.
' 2. Expand the first selected component and
'    expand and examine the Smart Feature folder.
'-------------------------------------------------------
Option Explicit
```

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim pCompSmart As Object
Dim pComp1 As Object
Dim pComp2 As Object
Dim pCompArr(1) As Object
Dim relcomp As Variant
Dim relfeat As Variant
Dim boundval As Variant
Dim boolstatus As Boolean
Dim retval As Boolean

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDockadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAssembly = swModel
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManagerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.Extensionkadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the component that you want to make smart
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("C-1@ABC_assembly",
"COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select the components that you want to associate with the Smart Component
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("B-1@ABC_assembly",
"COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.SelectByID2("A-2@ABC_assembly",
"COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pCompSmart = swSelMgr.GetSelectedObject6(1,
0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pComp1 = swSelMgr.GetSelectedObject6(2,
0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pComp2 = swSelMgr.GetSelectedObject6(3,
0)
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pCompArr(0) = pComp1
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
pCompArr(1) = pComp2
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}relcomp
= pCompArr
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create the Smart Componentkadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}retval
= swAssembly.CreateSmartComponent(pCompSmart,
(relcomp), (relfeat), False, Nothing, boundval)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}
End Sub
