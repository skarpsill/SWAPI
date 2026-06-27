---
title: "ModelDoc::SetUserPreferenceTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceTextFormat.htm"
---

# ModelDoc::SetUserPreferenceTextFormat

This method is obsolete
and has been superseded by[ModelDoc2::SetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__ISetUserPreferenceTextFormat.htm).

Description

This method sets the specified integer user
preference value on this document

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceTextFormat (userPreferenceValue, value)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference you wish to change as defined in swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Input: | (LPDISPATCH) value | Dispatch pointer to the TextFormat object you wish to give to the user
preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise. |

Syntax (COM)

status = ModelDoc->ISetUserPreferenceTextFormat
( userPreferenceValue, value, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User preference you wish to change as defined in swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Input: | (LPTEXTFORMAT) value | Pointer to the TextFormat object you wish to give to the user preference
specified in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is equivalent to using theTools,
Optionsmenu item in SolidWorks.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\obsoleteapi\ModelDoc\ModelDoc__SetUserPreferenceTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
