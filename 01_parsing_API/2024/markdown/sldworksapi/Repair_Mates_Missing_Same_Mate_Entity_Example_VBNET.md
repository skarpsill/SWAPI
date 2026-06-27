---
title: "Repair Mates Missing Same Mate Entity Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Repair_Mates_Missing_Same_Mate_Entity_Example_VBNET.htm"
---

# Repair Mates Missing Same Mate Entity Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim status As Boolean
        Dim errors As Integer

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swAssembly = swModel

        status = swModelDocExt.SelectByID2("Concentric1", "MATE", 0, 0, 0, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0562994754449733, -0.000769308980977712, 0.0081518960735707, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0516662570718722, 0.0153992319276881, 0.0199034517498262, True, 1, Nothing, 0)
        swAssembly.EditMate4(swMateType_e.swMateCONCENTRIC, swMateAlign_e.swMateAlignALIGNED, False, 0.001, 0.001, 0.001, 0.001, 0.001, 0, 0.5235987755983, 0.5235987755983, False, False, 0, True, errors)
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
