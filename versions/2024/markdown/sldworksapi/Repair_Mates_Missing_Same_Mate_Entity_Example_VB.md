---
title: "Repair Mates Missing Same Mate Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Repair_Mates_Missing_Same_Mate_Entity_Example_VB.htm"
---

# Repair Mates Missing Same Mate Entity Example (VBA)

This example shows how to repair all mates missing the same mate entity.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\RepairAssemMates.sldasm.
' 2. Click Close.
'
' Postconditions:
' 1. Selects the Concentric1 mate.
' 2. Selects a face on BoltHolder<1> and a face on Bolt<1>.
' 3. Edits and repairs all mates missing the same mate entity.
' 4. Examine the FeatureManager design tree.
'------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim status As Boolean
Dim errors As Long

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swAssembly = swModel
```

```
    status = swModelDocExt.SelectByID2("Concentric1", "MATE", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -5.62994754449733E-02, -7.69308980977712E-04, 8.1518960735707E-03, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -5.16662570718722E-02, 1.53992319276881E-02, 1.99034517498262E-02, True, 1, Nothing, 0)
    swAssembly.EditMate4 swMateType_e.swMateCONCENTRIC, swMateAlign_e.swMateAlignALIGNED, False, 0.001, 0.001, 0.001, 0.001, 0.001, 0, 0.5235987755983, 0.5235987755983, False, False, 0, True, errors
    swModel.ClearSelection2 True
```

```
End Sub
```
