var tiny = tiny || {};

tiny.config = {
    //
    // General
    //
    browsers: "msie,gecko,safari,opera",
    language: 'sv',
    mode: "specific_textareas",
    plugins: "fullscreen,inlinepopups,contextmenu,media,paste,safari",
    theme: "advanced",
    skin: "aino",

    //
    // Paste plugin
    //
    paste_block_drop: true,
    paste_strip_class_attributes: 'all',
    paste_remove_spans: true,
    
    //
    // Layout
    //
    height: '300',
    width: '600',

    //
    // Advanced theme 
    //
    theme_advanced_blockformats : "p,h2,h3",
    theme_advanced_buttons1: "formatselect,bold,italic,removeformat,|,bullist,numlist,|,link,unlink,|,image,media,|,pastetext,|,undo,redo,|,code,|,fullscreen",
    theme_advanced_buttons2: "",
    theme_advanced_buttons3: "",
    theme_advanced_path: true,
    theme_advanced_statusbar_location: "bottom",
    theme_advanced_toolbar_align: "left",
    theme_advanced_toolbar_location: "top",

    //
    // Configuration/cleanup 
    //
    apply_source_formatting: true,
    cleanup_on_startup: false,
    cleanup: true,
    convert_fonts_to_spans: true,
    convert_newlines_to_brs: false,
    element_format: "html",
    entity_encoding: "raw",
    fix_content_duplication: true,
    fix_list_elements: true,
    fix_nesting: true,
    fix_table_elements: true,
    forced_root_block: 'p',
    remove_redundant_brs: true,

    //
    // URL
    //
    relative_urls: false
}


