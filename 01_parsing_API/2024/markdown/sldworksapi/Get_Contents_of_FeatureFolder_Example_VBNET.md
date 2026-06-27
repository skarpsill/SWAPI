---
title: "Get Contents of FeatureFolder Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Contents_of_FeatureFolder_Example_VBNET.htm"
---

# Get Contents of FeatureFolder Example (VB.NET)

This example shows how to obtain the contents of feature folders.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document.
 ' 2. Right-click a feature in the FeatureManager design tree.
 ' 3. Select Add to New Folder, which adds the feature to
 '    the new folder.
 ' 4. Open the Immediate Window.
 '
 ' Postconditions: Inspect the Immediate Window.
 '------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swFeatMgr As FeatureManager
         Dim swFeat As Feature
         Dim swFeatFolder As IFeatureFolder
         Dim swFtrFolder As Feature
         Dim FeatType As String
         Dim FeatTypeName As String
         Dim Features As Object
         Dim i As  Long

         Dim featureArr(2) As Feature

         swModel = swApp.ActiveDoc
         swFeatMgr = swModel.FeatureManager

         swFeat = swModel.FirstFeature
         Do While Not swFeat Is  Nothing
             FeatType = swFeat.Name
             FeatTypeName = swFeat.GetTypeName2
             Dim temp As Long
             temp = InStr(1, FeatType, "EndTag", vbTextCompare)

             If (FeatTypeName = "FtrFolder" And temp = 0) Then
                 Debug.Print(FeatType & " [" & FeatTypeName & "]")
                 swFeatFolder = swFeat.GetSpecificFeature2
                 Features = swFeatFolder.GetFeatures
                 Debug.Print("    Number of Features: " & swFeatFolder.GetFeatureCount)
                 For i = 0 To (swFeatFolder.GetFeatureCount - 1)
                     swFtrFolder = Features(i)
                     Debug.Print("     Name of feature: " & swFtrFolder.Name)
                     Debug.Print("     Type of feature: " & swFtrFolder.GetTypeName2)
                 Next i
             End If
             swFeat = swFeat.GetNextFeature
         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
