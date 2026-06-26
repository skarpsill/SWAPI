---
title: "Move Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Bodies_Example_VBNET.htm"
---

# Move Bodies Example (VB.NET)

This example shows how to move all of the bodies in a part document.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Specified part document to open exists.
' 2. Run the macro.
'
' Postconditions: All of the bodies in the part document
' are moved to the specified location.
'
' NOTE: Because this part is used elsewhere, do not save
' any changes when closing it.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Sub SelectBodies(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal bodyArr As Object)
        ' Select and mark the bodies to move
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim body As Object
        Dim swBody As Body2
        Dim status As Boolean

        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData

        If (bodyArr Is Nothing) Then Exit Sub
        For Each body In bodyArr
            swBody = body
            swSelData.Mark = 1
            status = swBody.Select2(True, swSelData)
        Next body

    End Sub

    Sub Main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim bodyArr As Object
        Dim swFeatMgr As FeatureManager
        Dim swFeat As Feature
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swPart = swModel
        swFeatMgr = swModel.FeatureManager

        swModel.ClearSelection2(True)

        ' Get the bodies to move
        bodyArr = swPart.GetBodies2(swBodyType_e.swAllBodies, False)
        SelectBodies(swApp, swModel, bodyArr)

        ' Move the bodies
        swFeat = swFeatMgr.InsertMoveCopyBody2(0.1, 0.2, 0.3, 0.0#, 0.0#, 0.0#, 0.0#, 0.0#, 0.0#, 0.0#, False, 1)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
