---
title: "ModelDoc::GetUserPreferenceTextFormat"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetUserPreferenceTextFormat.htm"
---

# ModelDoc::GetUserPreferenceTextFormat

This
method is obsolete and has been superseded by[ModelDoc2::GetUserPreferenceTextFormat](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetUserPreferenceTextFormat.htm).

Description

This method gets the specified text format
user preference from this document.

Syntax (OLE Automation)

retval = ModelDoc.GetUserPreferenceTextFormat (userPreferenceValue, retval)

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-preference toggle you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the TextFormat object associated with
the specified userPreferenceValue setting. |

Syntax (COM)

status = ModelDoc->IGetUserPreferenceTextFormat
( userPreferenceValue, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | User-pPreference toggle you wish to get; for a complete and up-to-date
list of available options, see swUserPreferenceTextFormat_e |
| --- | --- | --- |
| Output: | (LPTEXTFORMAT) retval | Pointer to the TextFormat object associated with the specified userPreferenceValue
setting |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This method is the same as using theTools,
Optionsmenu item.

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetUserPreferenceTextFormat.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
