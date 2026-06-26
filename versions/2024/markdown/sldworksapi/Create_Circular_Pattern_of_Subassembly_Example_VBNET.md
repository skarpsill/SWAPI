---
title: "Create Circular Pattern of Subassembly Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Circular_Pattern_of_Subassembly_Example_VBNET.htm"
---

# Create Circular Pattern of Subassembly Example (VB.NET)

This example shows how to create a circular pattern of a subassembly.

```
'-------------------------------------------------------
' Preconditions: Verify that the assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects an edge for Direction 1.
' 3. Selects a subassembly to pattern.
' 4. Creates a circular pattern.
' 5. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'--------------------------------------------------------
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

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\distance linkage.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager
        status = swModelDocExt.SelectByID2("", "EDGE", 0.22639417933982, -0.194822643434378, 0.102086175644843, False, 2, Nothing, 0)
        status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
        swFeature = swFeatureManager.FeatureCircularPattern5(3, 2.0943951023932, False, "NULL", False, True, False, False, False, False, 0, 0, "NULL", False)
)
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
