---
title: "Replace Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Component_Example_VB.htm"
---

# Replace Component Example (VBA)

This example shows how to replace all instances of a component with a different component.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\assem1.sldasm.
' 2. Select testpart1<1> in the FeatureManager design tree.
' 3. Verify that the specified part exists.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Replaces all instances of the selected component with the
'    specified replacement component.
' 2. Examine the Immediate window, FeatureManager design tree,
'    and assembly.
'
' NOTE: Because the assembly is used elsewhere, do not save
' changes.
'-------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const fileName As String = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block.sldprt"
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelComp As SldWorks.Component2
    Dim status As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swSelComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
    Debug.Print "Old component = " & swSelComp.Name2
    status = swAssy.ReplaceComponents2(fileName, "", True, 0, True)
    Debug.Print "Replacement component = " & swSelComp.Name2
    Debug.Print "All instances of old component replaced? " & status
```

```
End Sub
```
