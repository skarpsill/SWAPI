---
title: "Create Bidirectional Linear Pattern Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Linear_Pattern_Example_VBNET.htm"
---

# Create Bidirectional Linear Pattern Example (VB.NET)

This example shows how to create a bidirectional linear pattern.

```
'----------------------------------------------------
' Preconditions: Verify that the part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the feature to pattern.
' 3. Selects the edges for Direction 1 and
'    Direction 2 for the bidirectional linear
'    pattern.
' 4. Creates a bidirectional linear pattern.
' 5. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager

        'Select feature to pattern
        status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)

        'Select edges for Direction 1 and Direction 2
        status = swModelDocExt.SelectByID2("", "EDGE", -0.0341223962029176, 0.0300321434688158, 0.0460303188361877, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.0436465176948104, 0.0301916139486593, 0.0114344277122314, True, 2, Nothing, 0)

        'Create linear pattern
        swFeature = swFeatureManager.FeatureLinearPattern5(3, 0.01, 3, 0.01, False, False, "NULL", "NULL", True, False, False, False, False, False, True, True, False, False, 0, 0, False, False)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
