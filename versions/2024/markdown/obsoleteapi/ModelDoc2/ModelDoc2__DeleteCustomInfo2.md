---
title: "ModelDoc2::DeleteCustomInfo2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__DeleteCustomInfo2.htm"
---

# ModelDoc2::DeleteCustomInfo2

This
method is obsolete and has been superseded by ModelDocExtension::CustomPropertyManager .

Description

This method deletes custom information that has been defined for the
document or the specified configuration.

Syntax (OLE Automation)

retval = ModelDoc2.DeleteCustomInfo2(
configuration, FieldName )

(Table)=========================================================

| Input: | (BSTR) configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Return: | (BOOL) retval | TRUE if deleted, FALSE if not |

Syntax (COM)

status = ModelDoc2->DeleteCustomInfo2(
configuration, FieldName, &retval)

(Table)=========================================================

| Input: | (BSTR )configuration | Name of the configuration (see Remarks ) |
| --- | --- | --- |
| Input: | (BSTR) FieldName | Name of custom information |
| Output: | (VARIANT_BOOL) retval | TRUE if deleted, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The configuration name should be the name of a configuration
in the document. If the custom information is found in the specified configuration,
then this method deletes that custom information. If the name is an empty
string, then this method deletes the custom information from the document.

Metadata type="DesignerControl" startspan
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
<param name="Items" value="ZReleaseNotes2001Plus$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__DeleteCustomInfo2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="ModelDoc2_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\ModelDoc2\ModelDoc2__DeleteCustomInfo2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
