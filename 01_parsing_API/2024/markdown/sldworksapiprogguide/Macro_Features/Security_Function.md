---
title: "Security Function"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Macro_Features/Security_Function.htm"
---

# Security Function

The security function for a macro feature is optional for a VBA-based
macro feature, but required for a COM-based macro feature. This function:

1. Optionally calls IFeature::GetDefinition to obtain the[IMacroFeatureData](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IMacroFeatureData.html)object from the input feature.
2. Optionally gets the properties of the IMacroFeatureData
  object.
3. Optionally processes the following information to ascertain security:

  - Security function input arguments
  - Macro feature data properties from step 2
4. Must return a security value that is a combination of the values
  in[swMacroFeatureSecurityOptions_e](swconst.chm::/SolidWorks.interop.swconst~SolidWorks.interop.swconst.swMacroFeatureSecurityOptions_e.html).
  (Steps 1-3 can determine at runtime what value to return, but you can also
  hardcode a static return value.)

**NOTE:**If you call IFeature::GetDefinition from this security
function, you may cause an infinite recursion, as the security function calls
itself to check whether the macro feature can be edited whenever
IFeature::GetDefinition is called on a macro feature. To prevent a possible
recursion, set a static global flag in the security function after you call
IFeature::GetDefinition the first time.

This following example illustrates a VBA-based security function that
hardcodes the return value (step 4 above):

Public Function swmSecurity(app As Variant,
part As Variant, feature As Variant) As Variant

' If the file security.txt exists, then
enable displaying a note

' for the macro feature

' See[IFeatureManager::InsertSecurityNote](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeatureManager~InsertSecurityNote.html)for more information about

' notes and macro features

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nSecurityOptions As swMacroFeatureSecurityOptions_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nSecurityOptions
= swMacroFeatureSecurityByDefault

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
fso As FileSystemObject

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(fso Is Nothing) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
fso = New Scripting.FileSystemObject

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(Not (fso Is Nothing)) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(fso.FileExists("C:\Test\MacroFeatureSamples\security.txt"))
Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nSecurityOptions
= nSecurityOptions Or swMacroFeatureSecurityEnableNote

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swmSecurity
= nSecurityOptions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Function
