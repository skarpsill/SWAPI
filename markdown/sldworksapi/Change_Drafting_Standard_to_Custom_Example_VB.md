---
title: "Change Drafting Standard to Custom Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Drafting_Standard_to_Custom_Example_VB.htm"
---

# Change Drafting Standard to Custom Example VB

## Change Drafting Standard to Custom Drafting Standard (VBA)

This example shows how to change the drafting standard to a custom drafting
standard.

```vb
'-------------------------------------------------
' Preconditions: Model document is open and a
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}SOLIDWORKS-supplied drafting standard is set.
'
' Postconditions: Drafting standard is set to the
' kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}specified custom drafting standard.
'-------------------------------------------------
Option Explicit

Dim swApp kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}As SldWorks.SldWorks
Dim swModel kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
Dim swModExt kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}As SldWorks.ModelDocExtension
Dim bRetVal kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}As Boolean
Dim sPath kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}As String
Dim sFileName kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}As String
Dim vDSNames kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}As Variant
Dim i kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}As Integer

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModExt = swModel.Extension

'Get current SOLIDWORKS-supplied drafting standard
Debug.Print "Current drafting standard..."
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}(Standard, NoOptionSpecified) before = " & swModExt.GetUserPreferenceInteger(SwConst.swDetailingDimensionStandard, SwConst.swDetailingNoOptionSpecified)
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}(StandardName, NoOptionSpecified) before = " & swModExt.GetUserPreferenceString(SwConst.swDetailingDimensionStandardName, SwConst.swDetailingNoOptionSpecified)
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"

' Get drafting standard names
' Only the SOLIDWORKS-supplied drafting standards
' are returned; any custom drafting standards are
' not returned
Debug.Print "SOLIDWORKS-supplied drafting standards..."
vDSNames = swModExt.GetDraftingStandardNames
PrintNames vDSNames
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"

' Load custom drafting standard
bRetVal = swModExt.LoadDraftingStandard("C:\test\MyANSI.sldstd") ' Substitute your custom drafting standard path and filename

' Get custom drafting standard just-specified
Debug.Print "Standard that custom drafting standard is based on or derived from..."
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}(Standard, NoOptionSpecified) after custom loaded = " & swModExt.GetUserPreferenceInteger(SwConst.swDetailingDimensionStandard, SwConst.swDetailingNoOptionSpecified)
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}(StandardName, NoOptionSpecified) after custom loaded = " & swModExt.GetUserPreferenceString(SwConst.swDetailingDimensionStandardName, SwConst.swDetailingNoOptionSpecified)
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"

' Get drafting standard names
' Remember, only the SOLIDWORKS-supplied drafting standards
' are returned; any custom drafting standards are
' not returned
Debug.Print "SOLIDWORKS-supplied drafting standards..."
vDSNames = swModExt.GetDraftingStandardNames
PrintNames vDSNames
Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}"

End Sub

Function PrintNames(ByVal vDSNames As Variant)
For i = LBound(vDSNames) To UBound(vDSNames)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}" & vDSNames(i)
Next i
End Function
```
