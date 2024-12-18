�
    �;gX	  �            
       ��  � d dl Z d dlZd dlmZ d dlmZmZ  ed��       ej                  Zej                  Z	ej                  Zej                  ZdZd� Zd� Zed	k(  r� ee�      Zes' ej&                  d
�        ee� de� d��        e�        	  ej&                  d
�        ee� de� de� de� d��      Z eee�      \  ZZ ee�       ern�> ej&                  d�       yy)�    N)�datetime)�Fore�initT)�	autoresetz!https://pastebin.com/raw/pdiDd2Rsc                 ��  � 	 t        j                  | �      }|j                  dk(  rlg }|j                  j	                  �       D ]K  }d|v s�|j                  d�      \  }}|j                  |j                  �       |j                  �       d��       �M |S t        t        � dt        � d��       g S # t        $ r'}t        t        � dt        � d|� ��       g cY d }~S d }~ww xY w)N��   �|)�password�expiry_date�[ERROR] z Gagal mengunduh daftar password.z'Tidak dapat mengunduh daftar password: )�requests�get�status_code�text�
splitlines�split�append�strip�print�red�white�	Exception)�url�response�	passwords�liner
   r   �es          �msgc.py�get_password_listr      s�   � ���<�<��$�����3�&��I� ���0�0�2���$�;�,0�J�J�s�O�)�H�k��$�$�(�.�.�2B�S^�Sd�Sd�Sf�%g�h� 3� ���S�E��%��(H�I�J��I��� ����X�e�W�$K�A�3�O�P��	���s+   �AB- �
AB- �B- �-	C�6C�C�Cc           	      �D  � t        j                  �       }|D ]v  }|d   }t        j                  |d   d�      }| |k(  s�'||k  r&dt        � dt        � d|j                  d�      � d�fc S dt        � d	t        � d
|j                  d�      � d�fc S  dt        � d	t        � d�fS )Nr
   r   z%Y-%m-%dTz
[SUCCESS] zPassword valid hingga �.Fr   z!Password sudah kedaluwarsa sejak zPassword tidak ditemukan.)r   �now�strptime�greenr   �strftimer   )�input_password�password_list�current_date�itemr
   r   s         r   �validate_passwordr*   #   s�   � ��<�<�>�L����
�#���'�'��]�(;�Z�H���X�%��{�*���w�j���7M�k�Nb�Nb�cm�Nn�Mo�op�q�q�q����X�e�W�4U�Va�Vj�Vj�ku�Vv�Uw�wx�y�y�y� � �S�E��%��(A�B�B�B�    �__main__z
cls||clearr   z6Tidak dapat melanjutkan karena daftar password kosong.�[�!z] zMasukkan password: zpython3 topup.py)r   �osr   �coloramar   r   �LIGHTRED_EXr   �LIGHTGREEN_EXr$   �LIGHTYELLOW_EX�yellow�WHITEr   �PASTEBIN_PASSWORD_URLr   r*   �__name__r'   �systemr   �exit�inputr&   �is_valid�message� r+   r   �<module>r>      s	  �� � 	� � � �t� �
��������	�	�	���
�
�� <� ��$
C� �z��%�&;�<�M����	�	�,�����X�e�W�$Z�[�\��� ���	�	�,���#��a��w�a��u�B�u�g�=P�Q�R��-�n�m�L���'��g���� � �B�I�I� �!�! r+   