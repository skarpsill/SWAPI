---
title: "Delete Attribute Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Attribute_Example_VBNET.htm"
---

# Delete Attribute Example (VB.NET)

This example shows how to delete the selected attribute.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects Cut-Extrude3.
' 3. Adds attribute att 1 to the selected feature.
' 4. Rebuilds the part.
' 5. Deletes attribute att 1.
' 6. Expand Cut-Extrude3 in the FeatureManager design tree
'    and examine the Immediate window to verify step 5.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        '1 = invisible
        '0 = visible
        Const CreateVisible As Integer = 0
        Const AttDefName As String = "XML_string"
        Const AttLenDimName As String = "att_name"
        Const AttLenValueName As String = "att_value"
        Const AttRootName As String = "att"
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Object
        Dim swEnt As Entity
        Dim swAttDef As AttributeDef
        Dim swAtt As SolidWorks.Interop.sldworks.Attribute = Nothing
        Dim swParamName As Parameter
        Dim swParamValue As Parameter
        Dim AttName As String = ""
        Dim i As Integer
        Dim bRet As Boolean
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        'Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\bearing.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select feature
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SelectByID2("Cut-Extrude3", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swEnt = swFeat

        'Set attribute att 1
        swAttDef = swApp.DefineAttribute(AttDefName)
        bRet = swAttDef.AddParameter(AttLenDimName, swParamType_e.swParamTypeString, 0.0#, 0)
        bRet = swAttDef.AddParameter(AttLenValueName, swParamType_e.swParamTypeDouble, 0.0#, 0)
        bRet = swAttDef.Register
        While swAtt Is Nothing
            ' Get a unique attribute name
            i = i + 1
            AttName = AttRootName + Str(i)
            swAtt = swAttDef.CreateInstance5(swModel, swEnt, AttName, CreateVisible, swInConfigurationOpts_e.swThisConfiguration)
        End While
        swParamName = swAtt.GetParameter(AttLenDimName)
        swParamValue = swAtt.GetParameter(AttLenValueName)
        bRet = swParamName.SetStringValue2(AttName & " - " & AttLenDimName, swInConfigurationOpts_e.swAllConfiguration, "")
        bRet = swParamValue.SetDoubleValue2(i * 10, swInConfigurationOpts_e.swAllConfiguration, "")
        If Not swAtt Is Nothing Then
            Debug.Print("Attribute " & AttName & " created.")
        Else
            Debug.Print("Attribute " & AttName & " not created.")
        End If

        swModel.ForceRebuild3(True)

        'Delete attribute att 1
        bRet = swModelDocExt.SelectByID2("att 1", "ATTRIBUTE", 0, 0, 0, False, 0, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swAtt = swFeat.GetSpecificFeature2
        AttName = swAtt.GetName
        bRet = swAtt.Delete(True)
        If bRet Then
            Debug.Print("Attribute " & AttName & " deleted.")
        Else
            Debug.Print("Attritute " & AttName & " not deleted.")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
