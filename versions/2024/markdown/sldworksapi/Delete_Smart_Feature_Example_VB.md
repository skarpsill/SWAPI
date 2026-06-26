---
title: "Delete a Smart Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Delete_Smart_Feature_Example_VB.htm"
---

# Delete a Smart Feature Example (VBA)

This example shows how to delete a feature from a Smart Component.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\holecube.sldprt.
' 2. Expand the Smart Feature and Features folders to verify that
'    Features contains two extrusion features.
'
' Postconditions:
' 1. Deletes one extrusion feature from the Features folder.
' 2. Expand the Smart Feature and Features folders to verify that
'    Features contains one extrusion feature.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim featMgr As SldWorks.FeatureManager
 Dim myFeature As SldWorks.Feature
 Dim swTrainAss As SldWorks.ModelDoc2
 Dim swSmartPart As SldWorks.ModelDoc2
 Dim swSCFD As SldWorks.SmartComponentFeatureData
 Dim selMgr As SldWorks.SelectionMgr
 Dim feat As SldWorks.Feature
 Dim feats As Variant
 Dim obj As Object
 Dim i As Long
 Dim count As Long
 Dim boolstatus As Boolean
Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swSmartPart = swApp.ActiveDoc
     Set featMgr = swSmartPart.FeatureManager
     feats = featMgr.GetFeatures(True)
     count = featMgr.GetFeatureCount(True)

    For i = 0 To count - 1
         Set myFeature = feats(i)
         If myFeature.Name = "Smart Feature" Then
             Set swSCFD = myFeature.GetDefinition

            ' Open the training assembly of the Smart Component
             ' Open the SmartComponent PropertyManager page to access its selection lists
             boolstatus = swSCFD.AccessSelections(True):

            Set swTrainAss = swApp.ActiveDoc
             Set selMgr = swTrainAss.SelectionManager

            Debug.Print "Number of features: " & selMgr.GetSelectedObjectCount2(swSmartComponentFeatures)
             Debug.Print "Number of components: " & selMgr.GetSelectedObjectCount2(swSmartComponentComponents)

            ' Get the first extrusion from the features selection list
             Set obj = selMgr.GetSelectedObject6(1, swSmartComponentFeatures)
             Set feat = obj

            ' To delete an extrusion feature from a Smart Component,
             ' re-select it in the Smart Features selection list
             boolstatus = feat.Select2(True, swSmartComponentFeatures)

            ' Modify the definition of the Smart Feature,
             ' close the training assembly, and rebuild the Smart Component
             boolstatus = myFeature.ModifyDefinition(swSCFD, swSmartPart, Nothing)
         End If
     Next

End Sub
```
