---
title: "ModelDoc::SetUserPreferenceStringValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceStringValue.htm"
---

# ModelDoc::SetUserPreferenceStringValue

This method is obsolete
and has been superseded by[ModelDoc2::SetUserPreferenceStringValue](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceStringValue.htm).

Description

This method sets various system default user
preference values. This method is intended for user preferences of type
string.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceStringValue (
userPreference, userPrefVal )

(Table)=========================================================

| Input: | ( long ) userPreference | User preference value you wish to set as defined
in swUserPreferenceStringValue_e |
| --- | --- | --- |
| Input: | ( BSTR ) userPrefVal | String value of the user preference specified
in userPreference |
| Return: | (BOOL) retval | TRUE if User Preference value was replaced |

Syntax (COM)

status = ModelDoc->SetUserPreferenceStringValue
( userPreference, userPrefVal, &retval )

(Table)=========================================================

| Input: | ( long ) userPreference | User preference value you wish to set as defined
in swUserPreferenceStringValue_e |
| --- | --- | --- |
| Input: | ( BSTR ) userPrefVal | the string value of the user preference specified
in userPreference |
| Output: | (VARIANT_BOOL) retval | TRUE if User Preference value was replaced |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using theTools,
Optionsmenu item in SolidWorks.

To use this method, choose one of the available
items from the swUserPreferenceStringValue_e enumeration. The value passed
in the userPrefVal argument will become the current system default value
for the user preference you are setting.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="SldWorks Method$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUserPreferenceStringValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__SetUserPreferenceStringValue.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
