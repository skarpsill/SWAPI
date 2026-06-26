---
title: "Insert Connection Point Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Connection_Point_Example_VBNET.htm"
---

# Insert Connection Point Example (VB.NET)

This example shows how to create a connection point for a tube for routing.

```
'---------------------------------------------------
' Preconditions:
' 1. Load the SOLIDWORKS Routing Add-in (click
'    Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Verify that the specified part document to open
'    exists.
'
' Postconditions:
' 1. Creates a connection point for a tube
'    using the selected edge.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatMgr As FeatureManager
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean

        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\routing-pipes\fittings\filter.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Select the edge for the connection point;
        ' remember to specify a value of 1 for
        ' the Mark parameter for a circular edge for
        ' a tube's connection point
        status = swModelDocExt.SelectByID2("", "EDGE", 0.001425156111225, 0.1755840982619, -0.09117938337181, False, 1, Nothing, 0)

        ' Insert a connection point for a tube
        swFeatMgr = swModel.FeatureManager
        Debug.Print("Connection point for tube created? " & swFeatMgr.InsertConnectionPoint(swConnectionPointType_e.swConnectionPoint_Tube, 0, True, 25.4 / 1000, 0.1, 0.2, 0.3, 0.4, "", 0, 0, False, "Specification", ""))
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
