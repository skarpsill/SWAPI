---
title: "Get All External References for Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_All_External_References_for_Drawing_Example_VBNET.htm"
---

# Get All External References for Drawing Example (VB.NET)

This example shows how to get the external references for a drawing document.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API
 '    Getting Started topic and ensure that the
 '    required DLLs are registered.
 ' 2. Copy and paste this module into a VB.NET
 '    console application in Microsoft Visual Studio.
 ' 3. Substitute the name of your drawing document that has at least one
 '    custom property for drawing_document_with_external_references.
 ' 4. Add the SolidWorks.Interop.swdocumentmgr.dll
 '    reference to the project.
 ' 5. Substitute your_license_code with your
 '    SOLIDWORKS Document Manager license key.
 ' 6. Compile and run this program in Debug mode.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Module Module1

     Sub main()

         Const sLicenseKey As String = "your_license_code" 'Specify your license key
         Const sDocFileName As String = "drawing_document_with_external_references"

         Dim swClassFact As SwDMClassFactory
         Dim swDocMgr As SwDMApplication
         Dim swDoc As SwDMDocument23
         Dim swSearchOpt As SwDMSearchOption
         Dim nDocType As Integer
         Dim nRetVal As Integer
         Dim vDependArr As Object
         Dim vDepend As Object
         Dim vBrokenRefs As Object
         Dim vIsVirtuals As Object
         Dim vTimeStamps As Object
         Dim vIsImported As Object
         Dim licenseType As Integer

         ' Determine if document is a drawing
         If InStr(LCase(sDocFileName), "slddrw") > 0 Then
             nDocType = SwDmDocumentType.swDmDocumentDrawing
         Else
             ' Not a drawings file,
             nDocType = SwDmDocumentType.swDmDocumentUnknown
             ' so do not open
             Exit Sub
         End If

         swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         swDocMgr = swClassFact.GetApplication(sLicenseKey)
         swSearchOpt = swDocMgr.GetSearchOptionObject
         swDoc = swDocMgr.GetDocument(sDocFileName, nDocType,  False, nRetVal) : Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone = nRetVal)

         Debug.Print("File = " & swDoc.FullName)

         licenseType = swDoc.GetLicenseType
          Debug.Print("License type as defined in swDMDocumentLicenseType_e: " & licenseType)

         Dim bsFileTime As String = ""
         Dim bsLWFileTime As String = ""
         swDoc.GetFileAvgTime(bsFileTime, bsLWFileTime)
         Debug.Print("File open time: " & bsFileTime)
         Debug.Print("Lightweight open time: " & bsLWFileTime)

         Dim custprops As Object
         custprops = swDoc.GetCustomPropertyNames()

         Dim isEditable As Boolean
         swDoc.IsCustomPropertyEditable(custprops(0), isEditable)
         Debug.Print("Custom property " & custprops(0) & " is editable: " & isEditable)

         vBrokenRefs = Nothing
         Dim brokenRef As SwDmReferenceStatus
         vIsVirtuals = Nothing
         Dim isVirtual As Boolean
         vTimeStamps =  Nothing
         Dim timeStamp As Double
         vIsImported = Nothing
         Dim isImported As String

         vDependArr = swDoc.GetAllExternalReferences5(swSearchOpt, vBrokenRefs, vIsVirtuals, vTimeStamps, vIsImported) : If IsNothing(vDependArr) Then Exit  Sub

         Debug.Print("External references")
         For Each vDepend In vDependArr
             Debug.Print("  " & vDepend)
         Next vDepend
         Debug.Print("Reference statuses as defined in swDmReferenceStatus")
         For Each brokenRef In vBrokenRefs
             Debug.Print("  " & brokenRef)
         Next brokenRef
         Debug.Print("Virtual components?")
         For Each isVirtual In vIsVirtuals
             Debug.Print("  " & isVirtual)
         Next isVirtual
         Debug.Print("Timestamps")
         For Each timeStamp In vTimeStamps
             Debug.Print("  " & timeStamp)
         Next timeStamp
           Debug.Print("Imported components (empty if component is not imported)")
         For Each isImported In vIsImported
             Debug.Print("  Imported component:  " & isImported)
         Next isImported
     End Sub
 End Module
```
