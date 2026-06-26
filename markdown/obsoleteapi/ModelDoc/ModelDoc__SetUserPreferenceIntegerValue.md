---
title: "ModelDoc::SetUserPreferenceIntegerValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__SetUserPreferenceIntegerValue.htm"
---

# ModelDoc::SetUserPreferenceIntegerValue

This method is obsolete
and has been superseded by[ModelDoc2::SetUserPreferenceIntegerValu](sldworksAPI.chm::/ModelDoc2/ModelDoc2__SetUserPreferenceIntegerValue.htm)e.

Description

This method sets various user preference integer values.

Syntax (OLE Automation)

retval = ModelDoc.SetUserPreferenceIntegerValue (userPreferenceValue, value)

(Table)=========================================================

| Input: | (long) userPreferenceValue | Toggle to change as defined by swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Input: | (long) value | Numeric value to give to the user preference specified in userPreferenceValue |
| Return: | (BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |

Syntax (COM)

status = ModelDoc->SetUserPreferenceIntegerValue
( userPreferenceValue, value, &retval )

(Table)=========================================================

| Input: | (long) userPreferenceValue | Toggle to change as defined by swUserPreferenceIntegerValue_e |
| --- | --- | --- |
| Input: | (long) value | Numeric value to give to the user preference specified in userPreferenceValue |
| Output: | (VARIANT_BOOL) retval | TRUE if the setting was changed successfully, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="16777215" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__SetUserPreferenceIntegerValue.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
