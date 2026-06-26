---
title: "Change Pitch of Helix Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Pitch_of_Helix_Example_VBNET.htm"
---

# Change Pitch of Helix Example (VB.NET)

This example shows how to change the pitch of a helix.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a helix feature.
' 2. Select the helix feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Modifies the pitch of selected helix feature.
' 2. Gets the name of helix feature, original pitch, and
'    modified pitch values.
' 3. Examine the Immediate window and graphics area.
'--------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swHelix As HelixFeatureData
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swHelix = swFeat.GetDefinition

        Debug.Print("Feature = " & swFeat.Name)
        Debug.Print("  Original pitch = " & swHelix.Pitch * 1000.0# & " mm")

        ' Change the pitch value
        swHelix.Pitch = 1.25 * swHelix.Pitch
        Debug.Print("  Modified pitch = " & swHelix.Pitch * 1000.0# & " mm")

        ' Apply the change
        bRet = swFeat.ModifyDefinition(swHelix, swModel, Nothing) : Debug.Assert(bRet)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>

    Public swApp As SldWorks

End Class
```
