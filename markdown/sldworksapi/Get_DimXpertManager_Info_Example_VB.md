---
title: "Get DimXpertManager Info Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_DimXpertManager_Info_Example_VB.htm"
---

# Get DimXpertManager Info Example (VBA)

This example shows the usage of several interfaces that
provide access to information on the DimXpertManager tab of the Management Panel in
SOLIDWORKS.

The IDimXpertManager interface exposes schema information
on the DimXpertManager tab.

This macro demonstrates several ways of acquiring IDimXpertManager
on an open document:

- ISelectionManager.GetSelectedObject6()
- IModelDocExtension.DimXpertManager
- IConfiguration.DimXpertManager

This macro also demonstrates how to get the features
and annotations displayed on the DimXpertManager tab using:

- ISelectionManager.GetSelectedObject6()
- IDimXpertManager.DimXpertPart

'---------------------------------------------------------------------------- ' Preconditions: ' 1. Open public_documents \samples\tutorial\api\cover_with_geometric_tolerances.sldprt . ' 2. Select the DimXpertManager tab in the Management Panel. ' 3. Open the Immediate window. ' 4. Add a reference to SOLIDWORKS version DimXpert type
library . ' ' Postconditions: Inspect the Immediate Window. ' ' NOTE: Because this part is used elsewhere, do not save changes. '----------------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As IModelDoc2
Dim swModelDocExt As IModelDocExtension
Dim swSelMgr As ISelectionMgr
Dim swConfig As IConfiguration
Dim swFeature As IFeature
Dim swAnn As IFeature
Dim swSchema As IDimXpertManager
Dim swDXPart As IDimXpertPart
Dim msgStr As String
Dim msgStr2 As String
Dim displaytype As swDimXpertTreeDisplay_eDim boolstatus As Boolean
Dim n as Long

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.**ActiveDoc**
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelDocExt = swModel.**Extension**
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.**SelectionManager**
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select a DimXpert schema using swSelectType_e.swSelSWIFTSCHEMA
type
kadov_tag{{<spaces>}}'boolstatus
= swModelDocExt.**SelectByID2**("Scheme15", "SWIFTSCHEMA",
0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertManager (swSchema) for the DimXpert schema using
ISelectionManager.GetSelectedObject6()
kadov_tag{{<spaces>}}'Set
swSchema = swSelMgr.GetSelectedObject6(1,
-1)kadov_tag{{<spaces>}}'Debug.Print
(swSchema.**SchemaName**) + " acquired through ISelectionManager"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertManager (swSchema) for a DimXpert schema using IModelDocExtension.DimXpertManager()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSchema =swModelDocExt.DimXpertManager("Default",
True)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
(swSchema.**SchemaName**) + " acquired through IModelDocExtension"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get IDimXpertManager (swSchema) for a DimXpert schema using IConfiguration.DimXpertManager()kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swConfig = swModel.**GetConfigurationByName**("Default")
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSchema =swConfig.DimXpertManager(True)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
(swSchema.**SchemaName**) + " acquired through IConfiguration"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.**SchemaName**) + " shows a "
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}displaytype
= swSchema.**TreeDisplay**
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(displaytype = swDimXpertTreeDisplay_Flat)
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + "flat display of information on DimXpert tab"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(displaytype = swDimXpertTreeDisplay_Annotation)
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + "annotation-based display of information on DimXpert tab"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(displaytype = swDimXpertTreeDisplay_Feature)
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr + "feature-based display of information on DimXpert tab"
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select a DimXpert annotation using swSelectType_e.swSelSWIFTANNOTATIONS
type
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.**SelectByID2**("Flatness1", "SWIFTANN",
0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
All DimXpert features and annotations returned by GetSelectedObject6 are
instances of IFeaturekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAnn = swSelMgr.GetSelectedObject6(1,
-1)kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Is Flatness1 an annotation or a feature?
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swAnn.IsDimXpertAnnotation())
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Flatness1 is an annotation"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(swAnn.IsDimXpertFeature()) Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Flatness1 is a feature"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get all DimXpert features and annotations using DimXpertPartkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDXPart = swSchema.DimXpertPartkadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Display all DimXpert annotations using IDimXpertManager.DimXpertPartkadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
annCount As Long
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}annCount
= swDXPart.**GetAnnotationCount**
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Total of "
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= annCount
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= msgStr + msgStr2 + " annotations in " + (swSchema.**SchemaName**)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
annotations As Variant
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
annotation As IDimXpertAnnotation
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}annotations
= swDXPart.GetAnnotationskadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.**SchemaName**) + " has the following annotations: "
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(annotations)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
annotation = annotations(n)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ (annotation.**Name**)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select another DimXpert feature using swSelectType_e.swSelSWIFTFEATURES
type
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= swModelDocExt.**SelectByID2**("Plane1", "SWIFTFEATURE",
0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFeature = swSelMgr.GetSelectedObject6(1,
-1)kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Is Plane1 an annotation or a feature?
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(swFeature.IsDimXpertFeature())
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Plane1 is a feature"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
(swFeature.IsDimXpertAnnotation())
Then
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Flatness1 is an annotation"
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Display all DimXpert features using IDimXpertManager.DimXpertPartkadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featCount As Long
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featCount
= swDXPart.**GetFeatureCount**
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= "Total of "
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr2
= featCount
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= msgStr + msgStr2 + " features in " + (swSchema.**SchemaName**)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
features As Variant
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
feature As IDimXpertFeature
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}features
=swDXPart.GetFeatureskadov_tag{{<spaces>}}
kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}msgStr
= (swSchema.**SchemaName**) + " has the following features: "
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
msgStr
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
n = 0 To UBound(features)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
feature = features(n)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
+ (feature.**Name**)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

End Sub
