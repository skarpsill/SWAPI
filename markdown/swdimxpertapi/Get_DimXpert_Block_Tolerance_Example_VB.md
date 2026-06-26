---
title: "Get DimXpert Block Tolerance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdimxpertapi/Get_DimXpert_Block_Tolerance_Example_VB.htm"
---

# Get DimXpert Block Tolerance Example (VBA)

This example shows how to get the following block tolerance
values:

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ASME

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ISO Code

```vb
'---------------------------------------------------------------------------
' Preconditions:
' kadov_tag{{<spaces>}}1. Open public_documents\samples\tutorial\api\shaft.sldprt.
' kadov_tag{{<spaces>}}2. Open an Immediate window.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Ensure that the latest SOLIDWORKS DimXpert type library is loaded
'    in Tools > References.
' kadov_tag{{<spaces>}}4. Ensure that the Microsoft Scripting Runtime library is loaded
'    in Tools > References.
'
' Postconditions:
' 1. Inspect the Immediate window to see the ISO code for the part.
' kadov_tag{{<spaces>}}2. Open public_documents\api\cover_with_geometric_tolerances.sldprt.
' kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3. Run this macro (F5).
' kadov_tag{{<spaces>}}4. Inspect the Immediate Window to see the ASME block tolerance values
'    for the part.
' 5. Logs tkadov_tag{{</spaces>}}he output of this macro in c:\temp\dimXpertInfo.txt.
' kadov_tag{{<spaces>}}6. kadov_tag{{</spaces>}}Inspect the Immediate window.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Option Explicit
Sub Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swapp As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swapp = Application.SldWorks
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Dim swModelDoc As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}Set swModelDoc = swapp.ActiveDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If swModelDoc Is Nothing Then
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim f As New FileSystemObject
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim textStr As TextStream
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set textStr = f.CreateTextFile("C:\temp\dimXpertInfo.txt", True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If textStr Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Error creating temp file."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Starting DimXpert log...", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call retrieve_info_text(swapp, textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}textStr.Close
End Sub
Private Sub log(text As String, textStr As TextStream)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print text
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}textStr.WriteLine (text)
End Sub
Private Sub retrieve_info_text(swapp As SldWorks.SldWorks, textStr As TextStream)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertMgr As SldWorks.DimXpertManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertMgr = swapp.IActiveDoc2.Extension.DimXpertManager(swapp.IActiveDoc2.IGetActiveConfiguration().Name, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Model: " & swapp.IActiveDoc2.GetPathName, textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertPartObj As dimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertPartObj = dimXpertMgr.dimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim dimXpertPart As SwDimXpert.dimXpertPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set dimXpertPart = dimXpertPartObj
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vAnnotations As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vAnnotations = dimXpertPart.GetAnnotations()
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("Block Tolerances...", textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call log("------------------------", textStr)
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call listBlockTolerances_text(dimXpertPart, textStr)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
End Sub
Private Sub listBlockTolerances_text(dimXpertPart As SwDimXpert.dimXpertPart, textStr As TextStream)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim blockTols As SwDimXpert.DimXpertBlockTolerances
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim lin1 As Double, lin1prec As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim lin2 As Double, lin2prec As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim lin3 As Double, lin3prec As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim ang As Double
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim isoCode As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set blockTols = dimXpertPart.GetBlockTolerances()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Not blockTols Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case blockTols.Type
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ASMEInch
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = blockTols.GetToleranceValues(lin1, lin1prec, lin2, lin2prec, lin3, lin3prec, ang)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Call log("swDimXpertBlockToleranceType_ASMEInch", textStr)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Call log( _
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}"Linear1: " + Format(lin1prec) + " Places = " + Format(lin1, "##0.000000") + " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}" + _
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}"Linear3: " + Format(lin3prec) + " Places = " + Format(lin3, "##0.000000") + vbNewLine + _
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}"Linear2: " + Format(lin2prec) + " Places = " + Format(lin2, "##0.000000") + " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}" + _
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}"Angular = " + Format(ang * 57.2957795130823, "##0.000000"), textStr)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case swDimXpertBlockToleranceType_ISO2768
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Call log("swDimXpertBlockToleranceType_ISO2768", textStr)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolstatus = blockTols.GetISO2768PartType(isoCode)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Select Case isoCode
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertISO2768PartType_Fine
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}Call log("General Tolerance: Fine", textStr)
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertISO2768PartType_Medium
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}Call log("General Tolerance: Medium", textStr)
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertISO2768PartType_Coarse
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}Call log("General Tolerance: Coarse", textStr)
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}Case swDimXpertISO2768PartType_VeryCoarse
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}Call log("General Tolerance: Very Coarse", textStr)
kadov_tag{{<spaces>}}                     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
End Sub
```
