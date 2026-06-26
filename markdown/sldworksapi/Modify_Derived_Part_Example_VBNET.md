---
title: "Modify Derived Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_Derived_Part_Example_VBNET.htm"
---

# Modify Derived Part Example (VB.NET)

This example shows how to insert and modify a derived part.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the part documents to open and insert exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Inserts a derived part in the part document
'    opened in step 1.
' 3. Changes some parameters of the derived part feature.
' 4. Examine the Immediate window.
'
' NOTE: Because both part documents are used elsewhere,
' do not save any changes.
'-----------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim swModelDocExt As ModelDocExtension
        Dim swComp As Component2
        Dim swSelMgr As SelectionMgr
        Dim swDerivedFeat As Feature
        Dim swFeat As Feature
        Dim swDerivedData As DerivedPartFeatureData
        Dim bRet As Boolean
        Dim fileName As String
        Dim derivedFileName As String
        Dim errors As Integer
        Dim warnings As Integer

        'Open part, insert another part, and select the derived part feature
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\holecube.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        derivedFileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
        swPart = swModel
        swFeat = swPart.InsertPart3(derivedFileName, swInsertPartOptions_e.swInsertPartImportSolids, "Default")
        swModel.ClearSelection2(True)
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SelectByID2("box", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        'Get the selected derived part feature
        swSelMgr = swModel.SelectionManager
        swDerivedFeat = swSelMgr.GetSelectedObject6(1, -1)
        swComp = swSelMgr.GetSelectedObjectsComponent3(1, -1)
        Debug.Print("Name of derived part feature = " & swDerivedFeat.Name)
        Debug.Print("")
        'Get and modify import planes with derived part
        bRet = TestImportPlane(swDerivedFeat, swModel, swComp)
        Debug.Print("")
        'Get and modify import absorbed sketches with derived part
        bRet = TestImportAbsorbedSketches(swDerivedFeat, swModel, swComp)
        Debug.Print("")
        'Get and modify import unabsorbed sketches with derived part
        bRet = TestImportUnAbsorbedSketches(swDerivedFeat, swModel, swComp)
        Debug.Print("")
        swDerivedData = swDerivedFeat.GetDefinition
        Debug.Print("Derived file's path and name = " & swDerivedData.PathName)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

    Function TestImportPlane(ByVal feat As Feature, ByVal doc As ModelDoc2, ByVal comp As Component2) As Boolean
        Dim featData As DerivedPartFeatureData
        Dim startVal As Boolean
        Dim boolstatus As Boolean

        featData = feat.GetDefinition
        startVal = featData.ImportPlane
        Debug.Print("Import planes with derived part? " & startVal)
        featData.ImportPlane = True
        Debug.Print("Modified import planes with derived part? " & featData.ImportPlane)
        boolstatus = feat.ModifyDefinition(featData, doc, comp)
        featData = Nothing
    End Function

    Function TestImportAbsorbedSketches(ByVal feat As Feature, ByVal doc As ModelDoc2, ByVal comp As Component2) As Boolean
        Dim featData As DerivedPartFeatureData
        Dim startVal As Boolean
        Dim boolstatus As Boolean

        featData = feat.GetDefinition
        startVal = featData.ImportAbsorbedSketches
        Debug.Print("Import absorbed sketches with derived part? " & startVal)
        featData.ImportAbsorbedSketches = True
        Debug.Print("Modified import absorbed sketches with derived part? " & featData.ImportAbsorbedSketches)
        boolstatus = feat.ModifyDefinition(featData, doc, comp)
        featData = Nothing
    End Function

    Function TestImportUnAbsorbedSketches(ByVal feat As Feature, ByVal doc As ModelDoc2, ByVal comp As Component2) As Boolean
        Dim featData As DerivedPartFeatureData
        Dim startVal As Boolean
        Dim boolstatus As Boolean

        featData = feat.GetDefinition
        startVal = featData.ImportUnAbsorbedSketches
        Debug.Print("Import unabsorbed sketches with derived part? " & startVal)
        featData.ImportUnAbsorbedSketches = True
        Debug.Print("Modified import unabsorbed sketches with derived part? " & featData.ImportUnAbsorbedSketches)
        boolstatus = feat.ModifyDefinition(featData, doc, comp)
        featData = Nothing
    End Function

End Class
```
