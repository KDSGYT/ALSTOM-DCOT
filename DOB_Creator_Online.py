import backend
import streamlit as st

                   
st.set_page_config(
    page_title="Alstom-DCOT",
    layout="wide",)

st.header('Alstom-DCOT')


def pdf_uploader(column, title, helper_text, label, key_prefix):
    reset_key = f'{key_prefix}_reset'
    if reset_key not in st.session_state:
        st.session_state[reset_key] = 0

    column.subheader(title)
    column.write(helper_text)
    uploaded_file = column.file_uploader(
        label,
        type=['pdf'],
        key=f'{key_prefix}_{st.session_state[reset_key]}'
    )
    if uploaded_file is not None:
        if column.form_submit_button('Remove file', key=f'remove_{key_prefix}'):
            st.session_state[reset_key] += 1
            st.rerun()

    return uploaded_file


with st.form("my_form"):
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    dob_cover_page   = pdf_uploader(col1, 'DOB Cover Page', 'Leave blank to use Default cover page', ' ', 'dob_cover_page')
    don_cover_page   = pdf_uploader(col2, 'DON Cover Page', 'Leave blank to use Default cover page', '  ', 'don_cover_page')
    gta              = pdf_uploader(col3, 'Greater Metro', '                                     ', '   ', 'gta')
    bala             = pdf_uploader(col4, 'Metrolinx Bala', '                                     ', '    ', 'bala')
    don              = pdf_uploader(col5, 'Metrolinx DON', '                                     ', '     ', 'don')
    cp_west          = pdf_uploader(col6, 'CPKC West', '                                     ', '      ', 'cp_west')
    cp_hamilton      = pdf_uploader(col7, 'CPKC Hamilton', '                                     ', '       ', 'cp_hamilton')
    metrolinx_guelph = pdf_uploader(col8, 'Metrolinx Guelph', '                                     ', '        ', 'metrolinx_guelph')
    goderich_exeter  = pdf_uploader(col9, 'DOB Goderich & Exeter Railway', '                                     ', '         ', 'goderich_exeter')

    st.divider()

    st.form_submit_button('Create Packages') 
    

if dob_cover_page is None:
    dob_cover_page = './PDFs/Permanent DOB  DON Coverpage.pdf'
if don_cover_page is None:
    don_cover_page = './PDFs/Permanent DOB  DON Coverpage.pdf' 

DOB_to_email_files =  [ gta, bala,
                        './PDFs/Predeparture Checklist Template  - 2025-12-22.pdf',
                        './PDFs/EHS Concern  Form updated PDF 10.04.2026.pdf',
                        './PDFs/Reversing Re-Spotting Checklist updated April 02 2026.pdf',
                        './PDFs/Re-spotting an Overshoot and the Application of CROR 115 at Grade Crossings.pdf',
                        './PDFs/En route job briefings - Rev Apr 16, 2026.pdf',
                        './PDFs/Station to Station Notepad.pdf',
                        './PDFs/12.15. DMU Transponder Loops - Job Aid.pdf',
                        don, cp_west, cp_hamilton,
                        './PDFs/CPKC Signal Authority Form (Apr10).pdf',
                        metrolinx_guelph,
                        goderich_exeter,
                        './PDFs/Radio Channel Guide July 23rd.pdf'
                        ]
DOB_to_print_files = [dob_cover_page] + DOB_to_email_files
don_package_files  = [don_cover_page, don, './PDFs/EHS Concern  Form updated PDF 10.04.2026.pdf', './PDFs/Radio Channel Guide July 23rd.pdf']
cp_package_files   = [cp_west, cp_hamilton]

# get desktop location and filenames
dob_print_output_file, dob_email_output_file, don_output_file, cp_output_file, metro_output_file = backend.create_file_names()

if cp_west is not None and cp_hamilton is not None:
    cp_package = backend.combine(cp_package_files)
    st.download_button( label=f'Download {cp_output_file}',
                        data=cp_package,
                        file_name=cp_output_file,
                        mime="application/pdf"    )

if metrolinx_guelph is not None:
    st.download_button( label=f'Download {metro_output_file}',
                        data=metrolinx_guelph,
                        file_name=metro_output_file,
                        mime="application/pdf"    )

if don is not None:
    don_package = backend.combine(don_package_files)
    st.download_button( label=f'Download {don_output_file}',
                        data=don_package,
                        file_name=don_output_file,
                        mime="application/pdf"    )


if None not in DOB_to_email_files:
    dob_email_package = backend.combine(DOB_to_email_files)
    st.download_button( label=f'Download {dob_email_output_file}',
                        data=dob_email_package,
                        file_name=dob_email_output_file,
                        mime="application/pdf"    )
    dob_print_package = backend.combine(DOB_to_print_files)
    st.download_button( label=f'Download {dob_print_output_file}',
                        data=dob_print_package,
                        file_name=dob_print_output_file,

                        mime="application/pdf"    )   

